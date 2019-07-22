# Food-Detection-Case-Study
To perform this study of food detection, the UECFOOD100 dataset was used, which contained images of japanese foods. The dataset also came with the bounding box information and the category information of the food. Due to memory constraints only a subset of images (nearly 1200) were considered. Since I did not have any GPUs at my disposal, all the models were trained using Google Colab. Each code used is a jupyter notebook with explanation for each cell.

 1.  0_food_detect_data   -   code to extract images and bounding box information
 
 2.  1_Food_detection_keras   -   code to perform food detection based on YOLO model trained from scratch (model has not learned properly)
 
 3.  2_Food_detect_pytorch   -   code to perform food detection by finetuning pretrained Faster RCNN (error occurred)
 
 4.  3_Food_detection_imageai  - pretrained YOLO model from ImageAI module was used for extracting objects and classification was performed using a                                                        simple CNN (obtained a validation/test accuracy of nearly 60%) 
 
