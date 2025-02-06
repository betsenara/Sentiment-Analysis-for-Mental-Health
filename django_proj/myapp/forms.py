from django import forms


class TextInputForm(forms.Form):
   text = forms.CharField(
       max_length=500,
       widget=forms.Textarea(attrs={"placeholder": "Enter text here...", "rows": 4}),
       label="Text Input"
   )
   """
   model_type = forms.ChoiceField(
       choices=[("1", "Model 1: Diagnosed Data"), ("2", "Model 2: Community-Sourced Data")],
       label="Choose a Model",
       required=True
   )
   """


class UserDiagnosisForm(forms.Form):
   diagnosed = forms.ChoiceField(
       choices=[
           ('no', 'No'),
           ('yes', 'Yes'),
           ('normal', 'Diagnosed as Normal'),
       ],
       label="Are you diagnosed?",
       required=True
   )
   diagnosis = forms.ChoiceField(
       choices=[
           ('', '--Select--'),
           ('Anxiety', 'Anxiety'),
           ('BDP', 'Borderline Personality Disorder (BDP)'),
           ('Bipolar', 'Bipolar'),
           ('Depression', 'Depression'),
           ('Personality Disorder', 'Personality Disorder'),
           ('Stress', 'Stress'),
           ('Suicidal', 'Suicidal'),
       ],
       label="What is the diagnosis?",
       required=False
   )
   text = forms.CharField(
       widget=forms.Textarea(attrs={"rows": 4, "placeholder": "Enter additional details..."}),
       label="Your Text",
       required=False
   )
