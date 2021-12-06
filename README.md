# Reproducibility Report of "Deep, complex, invertible networks for inversion of transmission effects in multimode optical fibres"

This repository is the official implementation of [Deep, complex, invertible networks for inversion of transmission effects in multimode optical fibres](https://papers.nips.cc/paper/2018/hash/148510031349642de5ca0c544f31b2ef-Abstract.html) by Oisín Moran et al., and the original code can be found <a href="https://github.com/rodms/opticalfibreml" target="_blank">here</a>. The goal in the original paper was to build a complex-valued neural network that can mimic the physics of a multi-mode fibre and restore the distorted images. When an image is sent through a multi-mode fibre, it will get distorted into a speckle image that is unrecognizable by human eyes. However, conventional methods to restore the images requires many optical instruments. Therefore, a neural network can greatly save time and complexity in restoring these speckle images.

First, here is what a motion picture looks like before (original) and after (speckle, or distorted) transmission through the multi-mode fibre, as well as the reconsructed movie by our neural network model that was not trained on this dataset before:

<table>
<tr>
  <td align="center">Original</td>
  <td align="center">Speckle (distorted)</td>
  <td align="center">Reconstructed</td>
</tr>
  <tr>
    <td align="center"><img src=/Reproducibility_report/gifs/orig_punc.gif width="200" height="200"></td>
    <td align="center"><img src=/Reproducibility_report/gifs/1m_112x112_punc_speckles.gif width="200" height="200"></td>
    <td align="center"><img src=/Reproducibility_report/gifs/punc_Complex_L2_reg_epoch_300_lamb_0.03.gif width="200" height="200"></td>
  </tr>
</table>

>This motion picture was not included in the training or validation sets, which shows that the network generalized very well after training.

## Model Description

Here is a quick overview of the main pipelines of the models we recreated from the original paper and used in this reproducibility report:

<table>
<tr>
  <td align="center">Inverse model</td>
  <td align="center">Multi-Res inverse model</td>
</tr>
  <tr>
    <td align="center"><img src=/Reproducibility_report/figures/Inverse_model_updated.PNG></td>
    <td align="center"><img src=/Reproducibility_report/figures/multi-res.PNG></td>
  </tr>
</table>

> Detailed description of all models can be found in our reproducibility report.

## Requirements

Main packages used to run our models in the reproducibility report:

```
CUDA 11.3.1
PyTorch 1.10.0
```
Hardware requirements:

<ul>
  <li>An NVIDIA GPU that supports CUDA 11.3.1 (we used a single RTX 3080 Ti)</li>
  <li>32 GB of system memory</li>
</ul>

## Training and Testing

We have three experiments:
-Part 1: Building all of the inverse model variants (7 models) with different dense layer types (complex-valued and real-valued), different regularization methods and different loss functions. 
-Part 2: Training one of our models with different speckle resolutions to check the effect of speckle resolutions on mean square error (MSE) results of the models.
-Part 3: Checking the generalization of the models by using a new dataset not seen during training (some shots taken from a movie, shown in the GIF above).

We have four four notebooks:
<ul>
  <li>Final_Paper_Pytorch_With_Comments_V1_All_parts.ipynb: It has all parts with part 1 models trained with linear activations for 300 epochs</li>
  <li>Final_Paper_Pytorch_With_Comments_V1_part1_600epochs.ipynb: It has part 1 models trained with linear activations for 600 epochs</li>
  <li>Final_Paper_Pytorch_With_Comments_V1_part1_1000epochs.ipynb: It has part 1 models trained with linear activations for 1000 epochs</li>
  <li>Final_Paper_Pytorch_With_Comments_V1_part1_relu_300epochs.ipynb: It has part 1 models trained with ReLU activations for 300 epochs</li>
  <li>Final_Paper_Pytorch_With_Comments_V2_part1_relu_1000epochs.ipynb: It has part 1 models trained with ReLU activations for 1000 epochs</li>  
</ul>

>Each notebook will take anywhere between 3 (300 epochs) to 10 (1000 epochs) hours to complete.

## Results

Here we divide all test results into three sections: tests with different layer types, regularizations and training loss functions, tests with different speckle resolutions, and tests on new datasets not seen during training.

### MSE testing results 
Here we include the training results from the seven models with different layer types, regularizations and training loss functions:
<img src=/Reproducibility_report/figures/Table4.PNG>

Example outputs from all seven models are shown as following:
<img src=/Reproducibility_report/figures/regularization_fig.PNG>


### Speckle resolution tests
Here are the MSE values obtained from tests with different speckle resolutions:
<img src=/Reproducibility_report/figures/Table6.PNG>

And here are example output images from tests with different speckle resolutions:
<img src=/Reproducibility_report/figures/multi-res_fig.PNG>

### New datasets not seen in training
The models generalize well to new datasets not seen in training, meaning that they represent the true inverse transmission matrix of the fiber. The short movie at the beginning of the page is an example (was not seen in training).
Here are some screenshots from it:
<img src=/Reproducibility_report/figures/still_shot.PNG>
> All figures and tables in this section can be found in our Reproducibility report, along with more detailed explanations.

### Results beyond those reported in the original paper
We found that increasing the number of epochs and using ReLU activation improved the performance signficantly as one would expect, yet the authors did not try that. The maximum MSE enhancement we got was 20.47% when using 1000 epochs and ReLU activation for Model No. 6.
<img src=/Reproducibility_report/figures/extra.PNG>


## Contributing
<a href="https://github.com/ahmed6795" target="_blank">Ahmed Khaled</a>, <a href="https://github.com/ZhimuG" target="_blank">Zhimu Guo</a>   \
Members of <a href="https://www.queensu.ca/physics/shastrilab/" target="_blank">Shastri Lab</a>,  \
<a href="https://www.queensu.ca/physics/" target="_blank">Department of Physics, Engineering Physics, and Astronomy</a>,  \
<a href="https://www.queensu.ca/" target="_blank">Queen's University</a>,  \
<a href="https://www.google.ca/maps/place/Queen's+University/@44.2252795,-76.4973299,17z/data=!3m1!4b1!4m5!3m4!1s0x4cd2ab0fccd925e9:0x268a8a4f5c257211!8m2!3d44.2252795!4d-76.4951412?hl=en" target="_blank">Kingston, ON K7L 3N6</a>
