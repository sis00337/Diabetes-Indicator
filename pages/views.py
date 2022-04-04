# pages/views.py
import os
import warnings
from django.shortcuts import render, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.views.generic import TemplateView
import pickle
import sklearn
import pandas as pd

warnings.filterwarnings("ignore")

yes_or_no = ["Yes", "No"]


def homePageView(request):
    return render(request, 'home.html',
                  {'mySex': ["Male", "Female"],
                   'myEducation': ["Never attended school or only kindergarten",
                                   "Grades 1 through 8 (Elementary)",
                                   "Grades 9 through 11 (Some high school)",
                                   "Grades 12 or GED (High school graduate)",
                                   "College 1 year to 3 years (Some college or technical school)",
                                   "College 4 years or more (College graduate)"],
                   'myIncome': ["less than $10,000", "$10,000 to less than $15,000", "$15,000 to less than $20,000",
                                "$20,000 to less than $25,000", "$25,000 to less than $35,000",
                                "$35,000 to less than $50,000", "$50,000 to less than $75,000",
                                "$75,000 or more"],
                   "myGeneralHealth": ["Excellent", "Very Good", "Good", "Fair", "Poor"],
                   "myHealthCare": yes_or_no,
                   "myNoDocCost": yes_or_no,
                   "myCigar": yes_or_no,
                   "myPhysicalActivity": yes_or_no,
                   "myFruit": yes_or_no,
                   "myVeggies": yes_or_no,
                   "myDiffWalk": yes_or_no,
                   "myBP": yes_or_no,
                   "myChol": yes_or_no,
                   "myCholCheck": yes_or_no,
                   "myStroke": yes_or_no,
                   "myHeartDisease": yes_or_no,
                   })


def aboutPageView(request):
    # return request object and specify page.
    return render(request, 'about.html')


def homePost(request):
    # Use request object to extract choice.

    sexChoice = -999
    age = -999
    bmi = -999
    eduChoice = -999
    incomeChoice = -999
    genHealthChoice = -999
    healthCareChoice = -999
    noDocChoice = -999
    alcohol = -999
    cigarChoice = -999
    physicalChoice = -999
    fruitChoice = -999
    veggiesChoice = -999
    diffWalkChoice = -999
    BPChoice = -999
    cholChoice = -999
    cholCheckChoice = -999
    strokeChoice = -999
    heartDiseaseChoice = -999
    mental = -999
    physicalHealth = -999

    try:
        # Extract value from request object by control name.
        sexStr = request.POST['sexChoice']
        ageStr = request.POST['age']
        bmiStr = request.POST['bmi']
        eduStr = request.POST['eduChoice']
        incomeStr = request.POST['incomeChoice']
        genHealthStr = request.POST['genHealthChoice']
        healthCareStr = request.POST['healthCareChoice']
        noDocStr = request.POST['noDocChoice']
        alcoholStr = request.POST['alcohol']
        cigerStr = request.POST['cigarChoice']
        physicalActStr = request.POST['physicalChoice']
        fruitStr = request.POST['fruitChoice']
        veggieStr = request.POST['veggiesChoice']
        diffWalkStr = request.POST['diffWalkChoice']
        BPStr = request.POST['BPChoice']
        cholStr = request.POST['cholChoice']
        cholCheckStr = request.POST['cholCheckChoice']
        strokeStr = request.POST['strokeChoice']
        heartDiseaseStr = request.POST['heartDiseaseChoice']
        mentalDayStr = request.POST['mental']
        physicalDayStr = request.POST['physicalHealth']

        # Crude debugging effort.
        sexChoice = str(sexStr)
        age = int(ageStr)
        bmi = round(float(bmiStr), 1)
        eduChoice = str(eduStr)
        incomeChoice = str(incomeStr)
        genHealthChoice = str(genHealthStr)
        healthCareChoice = str(healthCareStr)
        noDocChoice = str(noDocStr)
        alcohol = int(alcoholStr)
        cigarChoice = str(cigerStr)
        physicalChoice = str(physicalActStr)
        fruitChoice = str(fruitStr)
        veggiesChoice = str(veggieStr)
        diffWalkChoice = str(diffWalkStr)
        BPChoice = str(BPStr)
        cholChoice = str(cholStr)
        cholCheckChoice = str(cholCheckStr)
        strokeChoice = str(strokeStr)
        heartDiseaseChoice = str(heartDiseaseStr)
        mental = int(mentalDayStr)
        physicalHealth = int(physicalDayStr)

    # Enters 'except' block if integer cannot be created.
    except:
        return render(request, 'home.html', {
            'errorMessage': '*** The data submitted is invalid. Please try again. ***',
            'mySex': ["Male", "Female"],
            'myEducation': ["Never attended school or only kindergarten",
                            "Grades 1 through 8 (Elementary)",
                            "Grades 9 through 11 (Some high school)",
                            "Grades 12 or GED (High school graduate)",
                            "College 1 year to 3 years (Some college or technical school)",
                            "College 4 years or more (College graduate)"],
            'myIncome': ["less than $10,000", "$10,000 to less than $15,000", "$15,000 to less than $20,000",
                         "$20,000 to less than $25,000", "$25,000 to less than $35,000",
                         "$35,000 to less than $50,000", "$50,000 to less than $75,000",
                         "$75,000 or more"],
            "myGeneralHealth": ["Excellent", "Very Good", "Good", "Fair", "Poor"],
            "myHealthCare": yes_or_no,
            "myNoDocCost": yes_or_no,
            "myCigar": yes_or_no,
            "myPhysicalActivity": yes_or_no,
            "myFruit": yes_or_no,
            "myVeggies": yes_or_no,
            "myDiffWalk": yes_or_no,
            "myBP": yes_or_no,
            "myChol": yes_or_no,
            "myCholCheck": yes_or_no,
            "myStroke": yes_or_no,
            "myHeartDisease": yes_or_no,
        })
    else:
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results',
                                            kwargs={'sexChoice': sexChoice, 'age': age, 'bmi': bmi,
                                                    'eduChoice': eduChoice, 'incomeChoice': incomeChoice,
                                                    'genHealthChoice': genHealthChoice,
                                                    'healthCareChoice': healthCareChoice, 'noDocChoice': noDocChoice,
                                                    'alcohol': alcohol, 'cigarChoice': cigarChoice,
                                                    'physicalChoice': physicalChoice, 'fruitChoice': fruitChoice,
                                                    'veggiesChoice': veggiesChoice, 'diffWalkChoice': diffWalkChoice,
                                                    'BPChoice': BPChoice, 'cholChoice': cholChoice,
                                                    'cholCheckChoice': cholCheckChoice, 'strokeChoice': strokeChoice,
                                                    'heartDiseaseChoice': heartDiseaseChoice, 'mental': mental,
                                                    'physicalHealth': physicalHealth}, ))


def results(request, sexChoice, age, bmi, eduChoice, incomeChoice, genHealthChoice, healthCareChoice, noDocChoice,
            alcohol, cigarChoice, physicalChoice, fruitChoice, veggiesChoice, diffWalkChoice, BPChoice, cholChoice,
            cholCheckChoice, strokeChoice, heartDiseaseChoice, mental, physicalHealth):
    print("*** Inside reults()")
    with open('./model.pkl', 'rb') as f:
        loadedModel = pickle.load(f)
    # Create a single prediction.
    singleSampleDf = pd.DataFrame(columns=['HighBP', 'HighChol', 'CholCheck', 'BMI', 'Smoker', 'Stroke',
                                           'HeartDiseaseorAttack', 'PhysActivity', 'Fruits', 'Veggies',
                                           'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost', 'MentHlth', 'PhysHlth',
                                           'DiffWalk', 'Sex', 'Age_2.0', 'Age_3.0', 'Age_4.0', 'Age_5.0', 'Age_6.0',
                                           'Age_7.0', 'Age_8.0', 'Age_9.0', 'Age_10.0', 'Age_11.0', 'Age_12.0',
                                           'Age_13.0', 'GenHlth_2.0', 'GenHlth_3.0', 'GenHlth_4.0', 'GenHlth_5.0',
                                           'Education_2.0', 'Education_3.0', 'Education_4.0', 'Education_5.0',
                                           'Education_6.0', 'Income_2.0', 'Income_3.0', 'Income_4.0', 'Income_5.0',
                                           'Income_6.0', 'Income_7.0', 'Income_8.0'])

    values = [sexChoice, age, bmi, eduChoice, incomeChoice, genHealthChoice, healthCareChoice, noDocChoice,
              alcohol, cigarChoice, physicalChoice, fruitChoice, veggiesChoice, diffWalkChoice, BPChoice,
              cholChoice, cholCheckChoice, strokeChoice, heartDiseaseChoice, mental, physicalHealth]

    if sexChoice == "Female":
        sexChoice = 0
    else:
        sexChoice = 1

    if 18 <= age <= 24:
        age = 1
    elif 25 <= age <= 29:
        age = 2
    elif 30 <= age <= 34:
        age = 3
    elif 35 <= age <= 39:
        age = 4
    elif 40 <= age <= 44:
        age = 5
    elif 45 <= age <= 49:
        age = 6
    elif 50 <= age <= 54:
        age = 7
    elif 55 <= age <= 59:
        age = 8
    elif 60 <= age <= 64:
        age = 9
    elif 65 <= age <= 69:
        age = 10
    elif 70 <= age <= 74:
        age = 11
    elif 75 <= age <= 79:
        age = 12
    elif age >= 80:
        age = 13

    if eduChoice == "Never attended school or only kindergarten":
        eduChoice = 1
    elif eduChoice == "Grades 1 through 8 (Elementary)":
        eduChoice = 2
    elif eduChoice == "Grades 9 through 11 (Some high school)":
        eduChoice = 3
    elif eduChoice == "Grade 12 or GED (High school graduate)":
        eduChoice = 4
    elif eduChoice == "College 1 year to 3 years (Some college or technical school)":
        eduChoice = 5
    else:
        eduChoice = 6

    if incomeChoice == "less than $10,000":
        incomeChoice = 1
    elif incomeChoice == "$10,000 to less than $15,000":
        incomeChoice = 2
    elif incomeChoice == "$15,000 to less than $20,000":
        incomeChoice = 3
    elif incomeChoice == "$20,000 to less than $25,000":
        incomeChoice = 4
    elif incomeChoice == "$25,000 to less than $35,000":
        incomeChoice = 5
    elif incomeChoice == "$35,000 to less than $50,000":
        incomeChoice = 6
    elif incomeChoice == "$50,000 to less than $75,000":
        incomeChoice = 7
    else:
        incomeChoice = 8

    if genHealthChoice == "Excellent":
        genHealthChoice = 1
    elif genHealthChoice == "Very Good":
        genHealthChoice = 2
    elif genHealthChoice == "Good":
        genHealthChoice = 3
    elif genHealthChoice == "Fair":
        genHealthChoice = 4
    else:
        genHealthChoice = 5

    if healthCareChoice == "No":
        healthCareChoice = 0
    else:
        healthCareChoice = 1

    if noDocChoice == "No":
        noDocChoice = 0
    else:
        noDocChoice = 1

    if sexChoice == 0 and alcohol > 7:
        alcohol = 1
    elif sexChoice == 1 and alcohol > 14:
        alcohol = 1
    else:
        alcohol = 0

    if cigarChoice == "No":
        cigarChoice = 0
    else:
        cigarChoice = 1

    if physicalChoice == "No":
        physicalChoice = 0
    else:
        physicalChoice = 1

    if fruitChoice == "No":
        fruitChoice = 0
    else:
        fruitChoice = 1

    if veggiesChoice == "No":
        veggiesChoice = 0
    else:
        veggiesChoice = 1

    if diffWalkChoice == "No":
        diffWalkChoice = 0
    else:
        diffWalkChoice = 1

    if BPChoice == "No":
        BPChoice = 0
    else:
        BPChoice = 1

    if cholChoice == "No":
        cholChoice = 0
    else:
        cholChoice = 1

    if cholCheckChoice == "No":
        cholCheckChoice = 0
    else:
        cholCheckChoice = 1

    if strokeChoice == "No":
        strokeChoice = 0
    else:
        strokeChoice = 1

    if heartDiseaseChoice == "No":
        heartDiseaseChoice = 0
    else:
        heartDiseaseChoice = 1

    age_2 = 0
    age_3 = 0
    age_4 = 0
    age_5 = 0
    age_6 = 0
    age_7 = 0
    age_8 = 0
    age_9 = 0
    age_10 = 0
    age_11 = 0
    age_12 = 0
    age_13 = 0

    if age == 2:
        age_2 = 1
    elif age == 3:
        age_3 = 1
    elif age == 4:
        age_4 = 1
    elif age == 5:
        age_5 = 1
    elif age == 6:
        age_6 = 1
    elif age == 7:
        age_7 = 1
    elif age == 8:
        age_8 = 1
    elif age == 9:
        age_9 = 1
    elif age == 10:
        age_10 = 1
    elif age == 11:
        age_11 = 1
    elif age == 12:
        age_12 = 1
    elif age == 13:
        age_13 = 1

    genHealthChoice_2 = 0
    genHealthChoice_3 = 0
    genHealthChoice_4 = 0
    genHealthChoice_5 = 0

    if genHealthChoice == 2:
        genHealthChoice_2 = 1
    elif genHealthChoice == 3:
        genHealthChoice_3 = 1
    elif genHealthChoice == 4:
        genHealthChoice_4 = 1
    elif genHealthChoice == 5:
        genHealthChoice_5 = 1

    eduChoice_2 = 0
    eduChoice_3 = 0
    eduChoice_4 = 0
    eduChoice_5 = 0
    eduChoice_6 = 0

    if eduChoice == 2:
        eduChoice_2 = 1
    elif eduChoice == 3:
        eduChoice_3 = 1
    elif eduChoice == 4:
        eduChoice_4 = 1
    elif eduChoice == 5:
        eduChoice_5 = 1
    elif eduChoice == 6:
        eduChoice_6 = 1

    incomeChoice_2 = 0
    incomeChoice_3 = 0
    incomeChoice_4 = 0
    incomeChoice_5 = 0
    incomeChoice_6 = 0
    incomeChoice_7 = 0
    incomeChoice_8 = 0

    if incomeChoice == 2:
        incomeChoice_2 = 1
    elif incomeChoice == 3:
        incomeChoice_3 = 1
    elif incomeChoice == 4:
        incomeChoice_4 = 1
    elif incomeChoice == 5:
        incomeChoice_5 = 1
    elif incomeChoice == 6:
        incomeChoice_6 = 1
    elif incomeChoice == 7:
        incomeChoice_7 = 1
    elif incomeChoice == 8:
        incomeChoice_8 = 1

    singleSampleDf = singleSampleDf.append({'HighBP': BPChoice, 'HighChol': cholChoice, 'CholCheck': cholCheckChoice,
                                            'BMI': bmi, 'Smoker': cigarChoice, 'Stroke': strokeChoice,
                                            'HeartDiseaseorAttack': heartDiseaseChoice, 'PhysActivity': physicalChoice,
                                            'Fruits': fruitChoice, 'Veggies': veggiesChoice,
                                            'HvyAlcoholConsump': alcohol, 'AnyHealthcare': healthCareChoice,
                                            'NoDocbcCost': noDocChoice, 'MentHlth': mental, 'PhysHlth': physicalHealth,
                                            'DiffWalk': diffWalkChoice, 'Sex': sexChoice, 'Age_2.0': age_2,
                                            'Age_3.0': age_3, 'Age_4.0': age_4, 'Age_5.0': age_5, 'Age_6.0': age_6,
                                            'Age_7.0': age_7, 'Age_8.0': age_8, 'Age_9.0': age_9, 'Age_10.0': age_10,
                                            'Age_11.0': age_11, 'Age_12.0': age_12, 'Age_13.0': age_13,
                                            'GenHlth_2.0': genHealthChoice_2, 'GenHlth_3.0': genHealthChoice_3,
                                            'GenHlth_4.0': genHealthChoice_4, 'GenHlth_5.0': genHealthChoice_5,
                                            'Education_2.0': eduChoice_2, 'Education_3.0': eduChoice_3,
                                            'Education_4.0': eduChoice_4, 'Education_5.0': eduChoice_5,
                                            'Education_6.0': eduChoice_6, 'Income_2.0': incomeChoice_2,
                                            'Income_3.0': incomeChoice_3, 'Income_4.0': incomeChoice_4,
                                            'Income_5.0': incomeChoice_5, 'Income_6.0': incomeChoice_6,
                                            'Income_7.0': incomeChoice_7, 'Income_8.0': incomeChoice_8},
                                           ignore_index=True)


    features = ['Income_4.0', 'HvyAlcoholConsump', 'Age_12.0', 'Age_5.0', 'Veggies', 'Education_2.0', 'Education_3.0',
                'Smoker', 'Education_4.0', 'Age_2.0', 'Income_3.0', 'Age_4.0', 'CholCheck', 'Age_3.0', 'Age_10.0',
                'MentHlth', 'Age_11.0', 'GenHlth_3.0', 'Income_2.0', 'Stroke', 'Education_6.0', 'PhysActivity',
                'Income_8.0', 'GenHlth_2.0', 'GenHlth_5.0', 'PhysHlth', 'HeartDiseaseorAttack', 'GenHlth_4.0',
                'HighChol',
                'DiffWalk', 'BMI', 'HighBP']
    X = singleSampleDf[features]
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', 1000)

    # with open('./scalerX.pkl', 'rb') as f:
    #     loadedXScaler = pickle.load(f)
    # X_scaled = loadedXScaler.fit_transform(X)
    singlePrediction = loadedModel.predict(X)
    print("Single prediction: " + str(singlePrediction))

    keys = ['sexChoice', 'age', 'bmi',
            'eduChoice', 'incomeChoice',
            'genHealthChoice',
            'healthCareChoice', 'noDocChoice',
            'alcohol', 'cigarChoice',
            'physicalChoice', 'fruitChoice',
            'veggiesChoice', 'diffWalkChoice',
            'BPChoice', 'cholChoice',
            'cholCheckChoice', 'strokeChoice',
            'heartDiseaseChoice', 'mental',
            'physicalHealth', 'prediction']

    parameters = {name: value for name, value in zip(keys, values)}
    parameters['prediction'] = singlePrediction[0]

    return render(request, 'results.html', parameters)
