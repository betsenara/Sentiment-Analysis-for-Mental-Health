from django.shortcuts import render
from .models import UserDiagnosis
import requests
from django.conf import settings

def predict_mental_health_view(request):
    prediction = None
    error = None

    # Define mappings for model predictions
    model_1_mapping = {
        0: "Anxiety",
        1: "Bipolar",
        2: "Depression",
        3: "Normal",
        4: "Personality Disorder",
        5: "Stress",
        6: "Suicidal"
    }

    model_2_mapping = {
        0: "Anxiety",
        1: "Borderline Personality Disorder (BDP)",
        2: "Bipolar",
        3: "Depression"
    }

    # Clear session on GET request to start fresh
    if request.method == "GET":
        request.session.clear()

    elif request.method == "POST":
        if "text" in request.POST and "model_choice" in request.POST:
            # Step 1: Handle Prediction
            text = request.POST.get("text")
            model_choice = request.POST.get("model_choice")

            # Save text and model choice in the session for the next step
            request.session["text"] = text
            request.session["model_choice"] = model_choice

            # Make the API request for prediction
            #url = "http://localhost:8000/predict/"  # Update with the FastAPI endpoint
            url = settings.FASTAPI_URL  # When docker is used
            payload = {"text": text, "model_type": model_choice}

            try:
                response = requests.post(url, json=payload)
                if response.status_code == 200:
                    prediction = response.json().get("prediction")

                    # Map prediction to the appropriate category
                    if model_choice == "1" and prediction is not None:
                        prediction = model_1_mapping.get(int(prediction), "Unknown")
                    elif model_choice == "2" and prediction is not None:
                        prediction = model_2_mapping.get(int(prediction), "Unknown")

                    # Save the prediction in the session
                    request.session["prediction"] = prediction
                else:
                    error = response.json().get("detail", "Unexpected error")
            except requests.exceptions.RequestException as e:
                error = f"Request failed: {e}"

        elif "diagnosed" in request.POST:
            # Step 2: Handle Diagnosis
            diagnosed = request.POST.get("diagnosed")
            diagnosis = request.POST.get("diagnosis")

            print(f"diagnosed {diagnosed}")
            print(f"diagnosis {diagnosis}")

            # Retrieve text and model_choice from the session
            text = request.session.get("text")
            model_choice = request.session.get("model_choice")

            if not text or not model_choice:
                error = "Session data is missing. Please restart the process."
            else:
                # Save diagnosis to the database
                prediction = request.session.get("prediction")
                if diagnosed == "yes" and diagnosis:
                    UserDiagnosis.objects.create(text=text, diagnosis=diagnosis,predicted_category=prediction,model_choice=model_choice)
                elif diagnosed == "normal":
                    UserDiagnosis.objects.create(text=text, diagnosis="Normal",predicted_category=prediction,model_choice=model_choice)

                # Clear session data after saving the diagnosis
                request.session.flush()
                return render(request, "myapp/predict.html", {"message": "Diagnosis saved successfully!"})

    # Retrieve prediction from session for rendering
    prediction = request.session.get("prediction")

    return render(request, "myapp/predict.html", {"prediction": prediction, "error": error})



