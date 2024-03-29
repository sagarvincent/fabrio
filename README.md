# Python developer technical challenge

This repo contains the code for checking and identifying the correct model with reference to a target model. The data folder contains a target model and attempt files. Each file is in JSON format and contains the data for the models. Each model is parameterized by the `volume`, `face`,` bounding box minimum point`, and `bounding box maximum point`. The idea is to compare the models with respect to their volume, the model that has the least difference from the target model will be the correct attempt. This method may not yield the correct results if there is a better model that has an infinitesimally small difference more than other models but is otherwise better suited. Therefore we will add more steps to the checking.
  1. Check if the no. of faces of the attempt is the same as the no. of faces of the target model
  2. Decide on a threshold for the difference between volumes.
  3. Check the difference between areas of the corresponding faces.<br />
<br />
First, we shortlist the models that have the same no. of faces as the target model. Then, we will select the model as follows: The models are further shortlisted if the volume difference is below a threshold. Among these, the models are ranked based on the cumulative error in corresponding faces and the cumulative error in the bounding box dimension. Then the best model is selected from the two tables based on a selection algorithm. At each stage, if only one model is selected from the previous list, it is assumed to be the correct models.
