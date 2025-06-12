# Open E. Coli Model
Predicting Escherichia coli (E. coli) and reducing reliance on time consuming lab testing 

Introduction
===========================

This repository contains the code for an E. coli model constructed using open data, including the [Environment Agency (EA) dataset](https://environment.data.gov.uk/water-quality/view/download/new). The model monitors E. coli presence in water samples collected from across the UK by leveraging selected water quality 
parameters and correlation analysis to optimize prediction. 


Purpose and Functionality
--------

The model uses an AI-driven approach to estimate the concentration of E. coli and 
to classify E. coli levels in bathing water samples. It is designed to address the lag in traditional laboratory analysis and related costs by providing real-time insights for public health and environmental management. 


Motivation
-------------------------------

The prediction of Escherichia coli (E. coli) presence and concentration in recreational bathing waters is important to support public health, and environmental monitoring [5]. E. coli is a key indicator of faecal contamination and is commonly used to assess the microbial quality of surface waters. While on its own E. coli can pose a risk to human health, its detection also indicates the possible presence of a broader range of faecal pathogens, which may pose additional health risks to humans entering the water [11][12]. Traditional detection methods, while reliable, are often time-consuming and resource intensive. Monitoring E. coli is currently constrained by the time it takes to complete a laboratory test.

England currently has many registered bathing waters that require E. coli testing periodically during summer periods to monitor contamination and calculate annual bathing water classifications. The time associated with sampling and analysis often means that the results of tests can take more than 48 hours to be completed and made public. In combination with the periodical sampling and a lack of testing during the winter season, it becomes difficult for swimmers, bathers and other recreational users to decide if the water is safe to engage with before it is too late.
Knowing that bathing water was contaminated by E. coli 2 days ago is not very useful to swimmers or others interacting with a waterbody. If we can provide a trustworthy forecast of E. coli, we can improve people’s ability to make an informed decision before entering the water.

To address these challenges, this study explores the application of machine learning (ML) techniques to estimate E. coli levels in coastal bathing waters efficiently [1][5].

The models, and their associated performance metrics, presented in this repository is the first iteration of our ML-models addressing the challenges mentioned above. As River Deep Mountain AI continue, these models will be further developed and refined. The models presented here are therefore preliminary and should be considered as such.


RDMAI overview  
-------------------------------
River Deep Mountain AI is an innovation project funded by the Ofwat Innovation Fund working collaboratively to develop open-source AI/ML models that can inform effective actions to tackle waterbody pollution.  
  
The project consists of 6 core partners: Northumbrian Water, Cognizant Ocean, Xylem Inc, Water Research Centre Limited, The Rivers Trust and ADAS. The project is further supported by 6 water companies across the United Kingdom and Ireland. 


Data Summary
------------
The [EA dataset](https://environment.data.gov.uk/water-quality/view/landing) used in this model comprises:
- Over 68 million EA water quality samples from 2,582 locations (from the year 2000 until mid 2024). 157,000 of these samples include specific E. coli measurements.
- After filtering by selecting proxy parameters, approximately 21,000 samples are used for model development. 

Additional Data Sources:
- We used the European Space Agency and Copernicus Climate Change Global Land Cover (LC) map V2.1.1 of 2020. The land cover dataset provides a global map describing the land surface according to 22 classes, which have been defined using the United Nations Food and Agriculture Organisationʼs (UN FAO) Land Cover Classification System (LCCS). [Link to the LC Dataset.](https://cds.climate.copernicus.eu/datasets/satellite-land-cover?tab=overview)
- Open-Meteo, which is an open-source historical weather API, is used to fetch 
weather data. 19 hourly, 13 daily and 13 weekly weather features are generated. These weather data are incorporated into the model as environmental factors that can influence E. coli levels. [This is the link to Open-Meteo Historical Weather API Docs.](https://open-meteo.com/en/docs/historical-weather-api)


Directory Structure and Main Components
-----------------------------------------
- EColi_data.ipynb: Notebook outlining the ETL process: data acquisition, extraction, transformation, and loading.
- EColi_model.ipynb: Notebook for data preprocessing, model development, training and inference of both estimator and classifier, and performance evaluation.
- utils.py: Contains utility functions to streamline the model pipeline and reduce redundant code.
- Models folder: Includes the best performing estimator and classifier models.
- Data folder: Includes Final data generated by EColi_data.ipynb.
- Install.md: Installation guide
- CONTRIBUTING.md: Contributing to Open E. Coli Model


Model Design
------------

The model is comprised of two primary components: 
1. E. coli Intensity Estimator: Estimates the concentration of E. coli in water samples. 
2. E. coli Classifier: Uses a binary classification to flag high-risk samples, using a threshold of 1,000 CFU/100 ml (or 500 CFU/100 ml) in line with international guidelines. 

*The threshold of 1,000 CFU/100 ml is widely recognised as a critical benchmark for public health safety. 


Training Approaches
-------------------
Two main train and test split methodologies were adopted:

1. Random Geographic Split Training:
   - Train: 85% of catchments (sampling locations)
   - Test: rest unseen catchments
   - Usage: Suitable to check the performance on new, unseen locations.

2. Random Temporal Split Training:
   - Train: 85% of samples from selected locations
   - Test: 15% of samples
   - Usage: Suitable for further refinement within existing catchments.

Performance Analysis on Model V3.0
--------------------
Best Estimator Model:
- LGBMRegressor:
    - Accuracy: ~74.89% (geographical split)
    - Threshold for accuracy considered 1000 CFU/100ml.

Classifier Model:
- XGBClassifier:
    - Accuracy: ~78.35% (temporal split)
    - Demonstrates balanced precision, recall, and F1-score.

<img width="793" alt="Image" src="https://github.com/user-attachments/assets/a32799a6-baeb-4f59-aae2-13c5b00b942b" />


Model Details
-------------

Input Features: 
- Water Quality Parameters: Water Temperature, Suspended Solids, Ammonia (N), Nitrate, Nitrite, Phosphate. 
- Land Cover Data: ESA Copernicus land cover dataset with 22 classes based on the UN LCCS 2020. 
- Weather Data: Weather data from Open-Meteo web weather service, and observation date. 

Output: 
- E. coli Density (for estimator): In CFU/100 ml. 
- Severity Levels (for classifier):  
    - Low: < 1000 CFU/100ml
    - High: > 1000 CFU/100ml

Key Findings 
--------------------

- Performance Analysis suggests that the estimator model performs better in detecting high concentrations of E. coli (with over 80% accuracy), while only detecting 65% of low-level concentrations accurately. 
- Different from the estimator model, the classifier model performs better in detecting low concentrations of E. coli. 
- The lower performance on one class can be improved/solved to some extent after conducting hyperparameters tuning. 
- The performance drop for models trained on Geographical Split config compared to Temporal Split reflects the geographic limitations, suggesting that sampling locations/catchments have location-specific characteristics. 
- The numbers of samples vary across the sampling locations in the EA dataset. One key observation is that the model performs relatively better in sampling locations in which more samples are available. 



Limitations 
--------------------
The models outlined in this report are not finalised models ready for deployment as they remain under development. This model represents the first iteration released open source. The aim of the model release is to provide insight into the model development process and to share early insights. 
At this stage, the model still has several limitations and so remains development and experimental. Generated classifications or estimations by this model should not be considered as 
ground truths, but rather as a supportive informative/alerting tool. 
- **Imbalance in the data:** Due to the nature of E. coli contamination, the data used for training this models were primarily composed of samples containing low or no E. coli, with a smaller number of samples showing high concentrations of E. coli. This creates an inherent imbalance, and risk of bias, in the data and the model, which results in a model tendency to under-simulate E. coli. This under-simulation of E. coli by the model might affect its capacity to estimate high concentrations or risk of E. coli. Current performance of the models can be seen in EColi_model.ipynb. Moving forward, we aim to reduce any imbalance (e.g. adding additional E. coli samples). 
- **Transferability:** Currently the models are trained and tested in both temporal and geographical splits, with a notable decline in accuracy when testing the models on unseen geographical areas. This puts a considerable limitation on the current transferability of the models. As our work continues, we intend to reduce this limitation by introducing additional E. coli samples, adding additional relevant features and re- feature selection. 


Planned Improvements
--------------------
Future developments include:
- Explore more ML models to compare their performances. 
- Focus on adding Moderate Resolution Imaging Spectroradiometer (MODIS) satellite data within the creation of v4.0 of the models. 
- Re-feature selection: Develop “light” version to reduce reliance on water quality parameters and to increase the quantity of E. coli samples. 
- Validate the model on other datasets to assess generalisability. 
- Regular hyperparameter tuning. 
- Develop models to predict Intestinal Enterococci (I.E.). 


Conclusions
-------------

The E. coli model presented here represents a robust tool for estimating E. coli concentrations and for real-time categorization of  E. coli levels in coastal bathing waters. The model can support public health initiatives by enabling timely interventions based on predictive analytics. Future enhancements aim to improve accuracy and incorporate more comprehensive environmental data. It is worth noting that while the model predictions cannot assure watercourse safety, they can help identify a potential microbial hazard in water bodies. Generated/output classifications or estimations of our model should not be considered as assured experiments, but rather a supportive, informative/alerting tool. 

For further questions or support, please refer to the documentation or reach out to:
    hossein.darvishi@cognizant.com
    nicolai.tarp@cognizant.com

## Disclaimer
River Deep Mountain AI (“RDMAI”) is run by a collection of UK water companies and their technology partners. The entities currently participating in RDMAI are listed at the end of this section and they are collectively referred to in these terms as the “consortium”.

This section provides additional context and usage guidance specific to the artificial intelligence models and / or software (the “**Software**”) distributed under the MIT License. It does not modify or override the terms of the MIT License.  In the event of any conflict between this section and the terms of the MIT licence, the terms of the MIT licence shall take precedence.

#### 1. Research and Development Status
The Software has been created as part of a research and development project and reflects a point-in-time snapshot of an evolving project. It is provided without any warranty, representation or commitment of any kind including with regards to title, non-infringement, accuracy, completeness, or performance. The Software is for information purposes only and it is not: (1) intended for production use unless the user accepts full liability for its use of the Software and independently validates that the Software is appropriate for its required use; and / or (2) intended to be the basis of making any decision without independent validation. No party, including any member of the development consortium, is obligated to provide updates, maintenance, or support in relation to the Software and / or any associated documentation.
#### 2. Software Knowledge Cutoff
The Software was trained on publicly available data up to Mid 2024. It may not reflect current scientific understanding, environmental conditions, or regulatory standards. Users are solely responsible for verifying the accuracy, timeliness, and applicability of any outputs.
#### 3. Experimental and Generative Nature
The Software may exhibit limitations, including but not limited to:
 - Inaccurate, incomplete, or misleading outputs; 
 - Embedded biases and / or assumptions in training data;
 - Non-deterministic and / or unexpected behaviour;
 - Limited transparency in model logic or decision-making
 
Users must critically evaluate and independently validate all outputs and exercise independent scientific, legal, and technical judgment when using the Software and / or any outputs. The Software is not a substitute for professional expertise and / or regulatory compliance.
 
#### 4. Usage Considerations
 
 - Bias and Fairness: The Software may reflect biases present in its training data. Users are responsible for identifying and mitigating such biases in their applications.
 - Ethical and Lawful Use: The Software is intended solely for lawful, ethical, and development purposes. It must not be used in any way that could result in harm to individuals, communities, and / or the environment, or in any way that violates applicable laws and / or regulations.
 - Data Privacy: The Software was trained on publicly available datasets. Users must ensure compliance with all applicable data privacy laws and licensing terms when using the Software in any way.
 - Environmental and Regulatory Risk: Users are not permitted to use the Software for environmental monitoring, regulatory reporting, or decision making in relation to public health, public policy and / or commercial matters. Any such use is in violation of these terms and at the user’s sole risk and discretion.
 
#### 5. No Liability
 
This section is intended to clarify, and not to limit or modify, the disclaimer of warranties and limitation of liability already provided under the MIT License.
 
To the extent permitted by applicable law, users acknowledge and agree that:
 - The Software is not permitted for use in environmental monitoring, regulatory compliance, or decision making in relation to public health, public policy and / or commercial matters.
 - Any use of the Software in such contexts is in violation of these terms and undertaken entirely at the user’s own risk.
 - The development consortium and all consortium members, contributors and their affiliates expressly disclaim any responsibility or liability for any use of the Software including (but not limited to):
   - Environmental, ecological, public health, public policy or commercial outcomes
   - Regulatory and / or legal compliance failures
   - Misinterpretation, misuse, or reliance on the Software’s outputs
   - Any direct, indirect, incidental, or consequential damages arising from use of the Software including (but not limited to) any (1) loss of profit, (2) loss of use, (3) loss of income, (4) loss of production or accruals, (5) loss of anticipated savings, (6) loss of business or contracts, (7) loss or depletion of goodwill, (8) loss of goods, (9) loss or corruption of data, information, or software, (10) pure economic loss, or (11) wasted expenditure resulting from use of the Software —whether arising in contract, tort, or otherwise, even if foreseeable . 
 
Users assume full responsibility for their use of the Software, validating the Software’s outputs and for any decisions and / or actions taken based on their use of the Software and / or its outputs.

#### 6. Consortium Members  
 
1. Anglian Water Services Limited 
2. Southwest Water Limited 
3. Northern Ireland Water 
4. Wessex Water Limited
5. The Rivers Trust
6. RSK ADAS Limited
7. Water Research Centre Limited
8. Xylem
9. Northumbrian Water Limited
10. Cognizant Worldwide Limited

References
----------
1. WPGW - AI Driven System for Water Pollution: https://www.wpgw.org/ai-driven-system-aims-to-inform-public-of-immediate-health-risks-from-bacterial-water-pollution
2. UK Environment Agency Data Help: https://environment.data.gov.uk/bwq/profiles/help-understanding-data.html
3. US EPA E.coli Document: https://19january2017snapshot.epa.gov/sites/production/files/2015-09/documents/ecoli.pdf
4. WHO Recommendations on Water Quality: https://cdn.who.int/media/docs/default-source/wash-documents/who-recommendations-on-ec-bwd-august-2018.pdf?sfvrsn=5c9ce1e0_6
5. Seok Min Hong, Billie J. Morgan, Matthew D. Stocker, Jaclyn E. Smith, Moon S. Kim, Kyung Hwa Cho, Yakov A. Pachepsky,Using machine learning models to estimate Escherichia coli concentration in an irrigation pond from water quality and drone-based RGB imagery data,Water Research,Volume 260,2024.
6. S. Jozić and M. Šolić, ‘Effect of Environmental Conditions on &lt;i&gt;Escherichia coli&lt;/i&gt; Survival in Seawater’, &lt;i&gt;Escherichia coli&lt;/i&gt; - Recent Advances on Physiology, Pathogenesis and Biotechnological Applications. InTech, Jul. 12, 2017.
7. Stephen E. DeVilbiss, Meredith K. Steele, Leigh-Anne H. Krometis, Brian D. Badgley, Freshwater salinization increases survival of Escherichia coli and risk of bacterial impairment, Water Research, Volume 191, 2021.
8. Taabodi, M., Hashem, F.M., Oscar, T.P. et al. The Possible Roles of Escherichia coli in the Nitrogen Cycle. Int J Environ Res 13, 597–602 (2019).
9. Lim CH, Flint KP. The effects of nutrients on the survival of Escherichia coli in lake water. J Appl Bacteriol. 1989.
10. Wang L, Xu S, Li J. Effects of phosphate on the transport of Escherichia coli O157:H7 in saturated quartz sand. Environ Sci Technol. 2011
11. Minnesota Department of Health on E.coli: https://www.health.state.mn.us/diseases/ecoli/ecoli.html
12. Wang G, Doyle MP. Survival of enterohemorrhagic Escherichia coli O157:H7 in water. J Food Prot. 1998.
13. Rui Li, Gabriel Filippelli, Lixin Wang, Precipitation and discharge changes drive increases in Escherichia coli concentrations in an urban stream, Science of The Total Environment, Volume 886, 2023
