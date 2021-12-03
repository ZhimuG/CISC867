# opticalfibreml
Data and code for the paper "Deep, complex, invertible networks for inversion of transmission effects in multimode optical fibres" published at NIPS 2018

This repository accompanies the paper "Deep, complex, invertible networks for inversion of transmission effects in multimode optical fibres", Oisín Moran · Piergiorgio Caramazza · Daniele Faccio · Roderick Murray-Smith, published at NeurIPS 2018, Montreal Canada. 
https://papers.nips.cc/paper/7589-deep-complex-invertible-networks-for-inversion-of-transmission-effects-in-multimode-optical-fibres.pdf
(Submitted 18th May 2018, presented 4th Dec 2018).

We use complex-weighted, deep networks to invert the effects of multimode optical fibre distortion of a coherent input image. We generated experimental data based on collections of optical fibre responses to greyscale input images generated with coherent light, by measuring only image amplitude  (not amplitude and phase as is typical) at the output of 1m and 10m long, 105micrometre diameter multimode fibre. This data is made available as the *Optical fibre inverse problem* Benchmark collection. The experimental data is used to train complex-weighted models with a range of regularisation approaches. A *unitary regularisation* approach for complex-weighted networks is proposed which performs well in robustly inverting the fibre transmission matrix, which is compatible with the physical theory. A benefit of the unitary constraint is that it allows us to learn a forward unitary model and analytically invert it to solve the inverse problem. We demonstrate this approach, and outline how it has the potential to improve performance by incorporating knowledge of the phase shift induced by the spatial light modulator. 

It includes the data used, and code to reproduce the images and results in the paper. Due to GitHub limitations on data size, the data set can be found here: https://www.dropbox.com/sh/dulp8zag0v914bm/AAB0piQu2HZlblCQayNuptkCa?dl=0  
