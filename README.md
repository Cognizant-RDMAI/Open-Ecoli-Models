# Open E. coli Model
Predicting Escherichia coli (*E. coli*) and reducing reliance on time consuming laboratory testing.


Introduction
===========================

This repository contains the code for an *E. coli* model constructed using open data, including the [Environment Agency (EA) dataset](https://environment.data.gov.uk/water-quality/view/download/new). The model monitors *E. coli* presence in water samples collected from across the UK by leveraging selected water quality 
parameters and correlation analysis to optimise prediction. 


Purpose and Functionality
--------

The model uses an AI-driven approach to estimate the concentration of *E. coli* and 
to classify *E. coli* levels in bathing water samples. It is designed to address the lag in traditional laboratory analysis and related costs by providing real-time insights for public health and environmental management. 

Report Download
--------

Please download the Open E.Coli Model Report [here](https://github.com/Cognizant-RDMAI/Open-Ecoli-Models/tree/main/Supporting-documents).

### Benchmark Download:

River Deep Mountain AI models have been independently benchmarked by WRc and ADAS, against existing industry-standard tools. The benchmarking reports assess model performance, ‘ease-of-use’, time and cost requirements.Read the full report [here](https://github.com/Cognizant-RDMAI/Open-Ecoli-Models/tree/main/Supporting-documents).

### Whitepaper Download:

Please download the whitepaper [here](https://github.com/Cognizant-RDMAI/Open-Ecoli-Models/tree/main/Supporting-documents).


Motivation
-------------------------------

The prediction of Escherichia coli (*E. coli*) presence and concentration in recreational bathing waters is important to support public health, and environmental monitoring [5]. *E. coli* is a key indicator of faecal contamination, and is commonly used to assess the microbial quality of surface waters. While on its own *E. coli* can pose a risk to human health, its detection also indicates the possible presence of a broader range of faecal pathogens, which may pose additional health risks to humans entering the water [11][12]. Traditional detection methods, while reliable, are often time-consuming and resource intensive. Monitoring *E. coli* is currently constrained by the time it takes to complete a laboratory test.

England currently has many registered bathing waters that require *E. coli* testing periodically during summer periods to monitor contamination and calculate annual bathing water classifications. The time associated with sampling and analysis often means that the results of tests can take more than 48 hours to be completed and made public. In combination with the periodical sampling and a lack of testing during the winter season, it becomes difficult for periodic swimmers, bathers and other recreational users to obtain timely information on waterbody risks to human health.
Being warned that bathing water was contaminated by *E. coli* 2 days after they were exposed is not useful to swimmers or other recreational users. If we can provide a trustworthy forecast of *E. coli*, we can improve people’s ability to make an informed decision before entering the water.


To address these challenges, this study explores the application of machine learning (ML) techniques to estimate *E. coli* levels in bathing waters efficiently [1][5].

The models, and their associated performance metrics, presented in this repository represent the first iteration of our ML-models addressing the challenges mentioned above. As River Deep Mountain AI continue, these models will be further developed and refined. The models presented here are therefore preliminary and should be considered as such.


RDMAI overview  
-------------------------------
River Deep Mountain AI is an innovation project funded by the Ofwat Innovation Fund working collaboratively to develop open-source AI/ML models that can inform effective actions to tackle waterbody pollution.

Model Design
------------

The model is comprised of two primary components: 
1. *E. coli* Intensity Estimator: Estimates the concentration of *E. coli* in water samples. This ML-model capable of estimating the concentration of *E. coli* in CFU/100ml. This model can later be applied to classify the potential risk of E. coli, and later compare performance between the estimator and classifier approach.
2. *E. coli* Classifier: Uses a binary classification to flag high-risk samples, using a threshold of 1,000 CFU/100 ml (or 500 CFU/100 ml) in line with international guidelines. 

*The threshold of 1,000 CFU/100 ml is widely recognised as a critical benchmark for public health safety. On the other hand, the threshold of 500 CFU/100ml is used by the Environment Agency in coastal bathing waters [2, 14].

Furthermore, to make our models to be more widely applicable, we have decided to develop an advanced and a light version of our models. This involves training an advanced model with more features and a light version with fewer features, but more *E. coli* samples: 

1. Advanced: including Water quality, land cover, weather and MODIS features, and trained on  EA bathing waters sampling data for locations in England (EA). Accessing in-situ water quality features and other environmental features helps the model to achieve high performance in estimating *E. coli*. 

2. Light: including all features from advanced version, except water quality features, and trained on EA, Wales and Scotland bathing waters sampling data for locations in England (EA), Wales (NRW), and Scotland (SEPA). Dropping water quality features will make the model more accessible and practically robust as it does not require any sensory water quality samples. 


Data Summary
------------
The [EA dataset](https://environment.data.gov.uk/water-quality/view/landing) used in this model comprises:
1. Over 68 million EA water quality samples from 2,582 locations (from the year 2000 until mid 2024). 157,000 of these samples include specific *E. coli* measurements. After filtering by selecting proxy parameters, approximately 21,000 samples are used for the advanced model development. 
2. Weather: Open-Meteo, which is an open-source historical weather API, is used to fetch 
weather data. 19 hourly, 13 daily and 13 weekly weather features are generated. These weather data are incorporated into the model as environmental factors that can influence *E. coli* levels. [This is the link to Open-Meteo Historical Weather API Docs.](https://open-meteo.com/en/docs/historical-weather-api)
3. Land cover: We use Land cover CORINE (Coordination of Information on the Environment) dataset generated from year 2018 which provides the European continent map describing the land surface into 44 classes, ranging from broad forested areas to individual vineyards. [Link to data.](https://land.copernicus.eu/en/products/corine-land-cover)
4. [MODIS](https://modis.gsfc.nasa.gov/data/): or Moderate Resolution Imaging Spectroradiometer is a key instrument two satellites with a 500 m spatial resolution. The MODIS data has been implemented to provide our models with additional contextual information, to support classification and estimation of *E. coli* risks. This includes Leaf Area Index (LAI), Fraction of Photosynthetically Active Radiation (FPAR), Land Surface Temperature and Emissivity. 
5. *E. coli* samples from Natural Resources Wales (NRW)  
6. *E. coli* samples from Scottish Environment Protection Agency (SEPA) 

The advanced model relies extensively on the first four sources, and the light model combines all six sources, but excludes additional water quality parameters to increase to useable *E. coli* samples. 

Directory Structure and Main Components
-----------------------------------------
- EColi_data_v4_adv.ipynb: Notebook outlining the ETL process for the advance model: data acquisition, extraction, transformation, and loading.
- EColi_model_v4_adv.ipynb: Notebook for data preprocessing, model development, training and inference of both estimator and classifier, and performance evaluation of the advanced model.
- EColi_ALLUK_v4_light.ipynb: Notebook outlining the ETL process for the light model at the first part - data acquisition, extraction, transformation, and loading - and follows with data preprocessing, model development, training and inference of both estimator and classifier, and performance evaluation of the light model.
- EColi_data_val_advance.ipynb: Notebook outlining the validation set preperation process for the advance model.
- EColi_data_val_light.ipynb: Notebook outlining the validation set preperation process for the light model.
- EColi_model_v4_adv_validation.ipynb: Notebook for advanced model validation, performance evaluation of both estimator and classifier of the advanced model.
- EColi_model_v4_light_validation.ipynb: Notebook for light model validation, performance evaluation of both estimator and classifier of the light model.
- utils.py: Contains utility functions to streamline the model pipeline and reduce redundant code.
- requirements.txt: Python libraries required. 
- Install.md: Installation guide.
- CONTRIBUTING.md: Contributing to Open *E. coli* Model.
- LICENSE: Licensing information and usage rights.



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
   - Usage: Suitable for further refinement within existing catchments*. 

*It is known that E. coli concentration in the environment is a function of time. However, because the dataset consisted of sparse, irregularly collected samples from multiple monitoring locations, we considered the possibility of treating them as independent observations. To assess whether this was appropriate, we performed an autocorrelation analysis (accounting for uneven time gaps) to determine if past E. coli measurements were strongly predictive of future ones. The results of the analysis showed, on average, very weak autocorrelation, suggesting that individual observations can reasonably be treated as independent for modelling purposes. Based on this finding, we proceeded with a random temporal split for model training and testing.

Performance Analysis of Model V4.0 on Validation Set
--------------------
Best performing advanced model:
- XGBClassifier trained under temporal split:
    - Accuracy: ~80.43% for threshold 500 CFU/100ml 
    - Demonstrates somewhat balanced per-class precision, recall, and F1-score.

Best performing light model:
- XGBRegressor trained under temporal split:
    - Accuracy*: ~77.83%
    - Threshold for accuracy considered 500 CFU/100ml. 

*Accuracy metric is choosen here as the risk level classification is the main objective of Open *E. coli* model, and also it is a way to compare Estimator model against Classifier model.

Model Details
-------------
Input:
The table below shows the input parameters and their definitions:
| #  | Parameter             | Definition                                                                 | Models           |
|----|-----------------------|----------------------------------------------------------------------------|------------------|
| 1  | Time                  | Hour of day which the sample was taken                                     | Light/Advanced   |
| 2  | Landcover             | Dominant landcover class – label encoded                                   | Light/Advanced   |
| 3  | Agri                  | Percentage of agricultural areas                                           | Light/Advanced   |
| 4  | Forest                | Percentage of forest areas                                                 | Light/Advanced   |
| 5  | Grass                 | Percentage of seminatural areas                                            | Light/Advanced   |
| 6  | Wetland               | Percentage of wetland areas                                                | Light/Advanced   |
| 7  | Build                 | Percentage of artificial surfaces                                          | Light/Advanced   |
| 8  | Others                | Percentage of bare lands                                                   | Light/Advanced   |
| 9  | LST                   | Land surface temperature                                                   | Light/Advanced   |
| 10 | FPAR                  | Fraction of photosynthetically active radiation                            | Light/Advanced   |
| 11 | EMIS31                | Land surface emissivity at band 31                                         | Light/Advanced   |
| 12 | LAI                   | Leaf area index                                                            | Light/Advanced   |
| 13 | Temperature_11am      | Air temperature at 2 meters above ground at 11 am of sample date           | Light/Advanced   |
| 14 | Humidity_11am         | Air Humidity at 11 am of sample date                                       | Light/Advanced   |
| 15 | Windspeed_11am        | Wind speed at 10 or 100 meters above ground at 11 am of sample date        | Light/Advanced   |
| 16 | Windgusts_11am        | Gusts at 10 meters above ground at 11 am of sample date                    | Light/Advanced   |
| 17 | Winddirection_11am    | Wind direction at 10 or 100 meters above ground at 11 am of sample date    | Light/Advanced   |
| 18 | Precipitation_11am    | Total precipitation (rain, showers, snow) sum at 11 am of sample date      | Light/Advanced   |
| 19 | Rain_11am             | Liquid precipitation at 11 am of sample date                               | Light/Advanced   |
| 20 | Snowfall_11am         | Hourly snowfall sum at 11 am of the sampling date                          | Light/Advanced   |
| 21 | Cloudcover_11am       | Total cloud cover as an area fraction at 11 am of the sampling date        | Light/Advanced   |
| 22 | Pressure_msl_11am     | Atmospheric air pressure reduced to mean sea level (msl) or surface        | Light/Advanced   |
| 23 | Soil_temp_7cm         | Average temperature of different soil levels below ground                  | Light/Advanced   |
| 24 | Soil_moist_7cm        | Average soil water content as volumetric mixing ratio at 0-7cm depths      | Light/Advanced   |
| 25 | Vap_press_def         | Vapor Pressure Deficit                                                     | Light/Advanced   |
| 26 | Et0_fao_evap          | ET₀ Reference Evapotranspiration of a well watered grass field (11 am)     | Light/Advanced   |
| 27 | Sun_duration          | Number of seconds of sunshine per hour                                     | Light/Advanced   |
| 28 | Global_tilted_irr     | Total radiation received on a tilted pane as average                       | Light/Advanced   |
| 29 | Short_rad             | Shortwave solar radiation as average at 11 am of sample date               | Light/Advanced   |
| 30 | Dir_rad               | Direct solar radiation as average at 11 am of sample date                  | Light/Advanced   |
| 31 | Dew_point_2m          | Dew point temperature at 2 meters above ground at 11 am of sample date     | Light/Advanced   |
| 32 | Temp_min              | Daily minimum temperature at the sampling date                             | Light/Advanced   |
| 33 | Temp_max              | Daily maximum temperature at the sampling date                             | Light/Advanced   |
| 34 | Precipitation_sum     | Daily precipitation sum at the sampling date                               | Light/Advanced   |
| 35 | Rain_sum              | Daily rain sum at the sampling date                                        | Light/Advanced   |
| 36 | Snowfall_sum          | Daily snowfall sum at the sampling date                                    | Light/Advanced   |
| 37 | Windspeed_max         | Daily windspeed max at the sampling date                                   | Light/Advanced   |
| 38 | Windgusts_max         | Daily wind gusts max at the sampling date                                  | Light/Advanced   |
| 39 | Winddirection_dominant| Daily wind dominant direction at the sampling date                         | Light/Advanced   |
| 40 | Precipitation_hours   | Daily Precipitation hours sum at the sampling date                         | Light/Advanced   |
| 41 | Sunshine_duration_d   | Total number of seconds of sunshine per day                                | Light/Advanced   |
| 42 | Daylight_duration_d   | Number of seconds of daylight per day                                      | Light/Advanced   |
| 43 | Short_rad_sum_d       | Daily shortwave solar radiation as average at sample date                  | Light/Advanced   |
| 44 | Et0_fao_evap_d        | ET₀ Reference Evapotranspiration of a well watered grass field (daily)     | Light/Advanced   |
| 45 | Temp_min7             | Average minimum weekly temperature                                         | Light/Advanced   |
| 46 | Temp_max7             | Average maximum weekly temperature                                         | Light/Advanced   |
| 47 | Precipitation_sum7    | Weekly precipitation sum at the sampling date                              | Light/Advanced   |
| 48 | Rain_sum7             | Weekly rain sum at the sampling date                                       | Light/Advanced   |
| 49 | Snowfall_sum7         | Weekly snowfall sum at the sampling date                                   | Light/Advanced   |
| 50 | Windspeed_max7        | Average weekly windspeed max at the sampling date                          | Light/Advanced   |
| 51 | Windgusts_max7        | Average weekly wind gusts max at the sampling date                         | Light/Advanced   |
| 52 | Winddirection_dom7    | Average weekly wind dominant direction at the sampling date                | Light/Advanced   |
| 53 | Precipitation_hours7  | Weekly Precipitation hours sum at the sampling date                        | Light/Advanced   |
| 54 | Sunshine_duration_d7  | Total number of seconds of sunshine per week                               | Light/Advanced   |
| 55 | Daylight_duration_d7  | Total number of seconds of daylight per week                               | Light/Advanced   |
| 56 | Short_rad_sum_d7      | Weekly sum of daily shortwave solar radiation as average                   | Light/Advanced   |
| 57 | Et0_fao_evap_d7       | Weekly sum of ET₀ Reference Evapotranspiration of a grass field            | Light/Advanced   |
| 58 | Distance_to_coast     | Distance to the closest coast                                              | Light/Advanced   |
| 59 | Season                | Season of the sample                                                       | Light/Advanced   |
| 60 | Temp Water            | Water temperature                                                          | Advanced         |
| 61 | Sld Sus@105C          | Solids, Suspended at 105 Celsius degrees                                   | Advanced         |
| 62 | Ammonia(N)            | Ammoniacal Nitrogen as N                                                   | Advanced         |
| 63 | Nitrate-N             | Nitrate as N                                                               | Advanced         |
| 64 | Nitrite-N             | Nitrite as N                                                               | Advanced         |
| 65 | Phosphate             | Phosphate :- (TIP)                                                         | Advanced         |


Output: 
- *E. coli* density (for estimator): In CFU/100ml. 
- Severity levels (for classifier and estimator):  
    - Low: < 1000 (or 500) CFU/100ml 
    - High: > 1000 (or 500) CFU/100ml


Key Findings 
--------------------
- All final version 4 models perform significantly better than earlier baselines (version 1 through 3). 
- Although accuracy is high, imbalance performance is observed which suggest most of models fail to generalize to unseen EA data — possibly due to many possibilities, including: 
   - overfitting 
   - data imbalance 
   - important features are missing
   - natural variability in E. coli is too high to predict reliably at fine granularity
   - or significant distribution shift in features.
- Best performing light model is XGBRegressor trained over temporal split. The model performance is more reliable when 500 cfu/100ml is chosen as threshold, even though, its accuracy declines slightly to 77.83% with reducing threshold due to balanced performance per-class.
- Best performing advanced model is XGBClassifier trained over temporal split with accuracy up to 80.43% (for threshold 500 cfu/100ml). This model is chosen due to its balanced performance.
- Prioritize advanced XGBClassifier for practical deployment. When in-situ water quality data is not available, light XGBRegressor is prioritized.
- We tried data augmention to solve the imbalance in the dataset and perfromance, but no visible improvement in performance has been seen.



Limitations 
--------------------
The models outlined in this report are not finalised models ready for deployment as they remain under development. This model represents the first iteration released open source. The aim of the model release is to provide insight into the model development process and to share early insights. 
At this stage, the model still has several limitations and so remains development and experimental. Generated classifications or estimations by this model should not be considered as ground truths, but rather as a supportive informative/alerting tool. 

- **Imbalance in the data:** Due to the nature of *E. coli* contamination, the data used for training this models were primarily composed of samples containing low or no *E. coli*, with a smaller number of these samples showing high concentrations of *E. coli*. This creates an inherent imbalance, and risk of bias, in the data and the model, which results in a model tendency to under-simulate *E. coli*. This under-simulation of *E. coli* by the model might affect its capacity to estimate high concentrations or risk of *E. coli*. Current performance of the models can be seen in EColi_model.ipynb. Moving forward, we aim to reduce any imbalance (e.g. adding additional *E. coli* samples). 

- **Transferability:** Currently the models are trained and tested in both temporal and geographical splits, with a notable decline in accuracy when testing the models on unseen geographical areas. This puts a considerable limitation on the current transferability of the models. As our work continues, we intend to reduce this limitation by introducing additional *E. coli* samples, adding additional relevant features and re- feature selection. 

- **Inland and coastal bathing waters:** While the model is trained on all bathing waters, both inland and coastal, we expect it to perform better on coastal waters. This is partly because different environmental factors (e.g. salinity) in coastal and inland areas, leading to more stable *E. coli* patterns in coastal compared to inland sites where sewage and runoff impacts can be more localized and variable.

- **Model Bias Toward Majority Class:** Except for advanced XGBClassifier, rest models relatively show high FN o validation set. High FN/FP often indicates the model favors the majority ("safe") class.

- **Threshold Sensitivity:** Changing thresholds significantly affects FN/FP balance.



Future Improvement Recommendations
--------------------
1. To reduce False negatives (FN) we recommend: 
   - Class balancing (resampling techniques). 
   - Adjusting decision thresholds. 
   - Cost-sensitive training might be helpful. 

2. Investigate ensemble strategies (e.g., regression + classification pipeline). 

3. Add uncertainty estimation or confidence intervals — especially important due to natural noise in environmental data. 

4. Consider more related features. 


Conclusions
-------------

The *E. coli* model presented here represents a robust tool for estimating *E. coli* concentrations and for real-time categorisation of  *E. coli* levels in bathing waters. The model can support public health initiatives by enabling timely interventions based on predictive analytics. Future enhancements aim to improve accuracy and incorporate more comprehensive environmental data. It is worth noting that while the model predictions cannot assure watercourse safety, they can help identify a potential microbial hazard in water bodies. Generated/output classifications or estimations of our model should not be considered as assured experiments, and the model should be considered a supportive information/alerting tool.

For further questions or support, please refer to the documentation or reach out to:
    nicolai.tarp@cognizant.com
    maryam.bilal@cognizant.com


## Disclaimer
River Deep Mountain AI (“RDMAI”) consists of 10 parties. The parties currently participating in RDMAI are listed at the end of this section and they are collectively referred to in these terms as the “consortium”.

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
 
1. Northumbrian Water Limited
2. Cognizant Worldwide Limited
3. Xylem Water Solutions UK Limited
4. Water Research Centre Limited
5. RSK ADAS Limited
6. The Rivers Trust
7. Wessex Water Limited
8. Northern Ireland Water
9. Southwest Water Limited
10. Anglian Water Services Limited


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

14. UK The Bathing Water Regulations:
https://www.legislation.gov.uk/uksi/2013/1675
