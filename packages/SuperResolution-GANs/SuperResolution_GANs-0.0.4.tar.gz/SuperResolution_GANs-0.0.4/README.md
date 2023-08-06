# Super Resolution Image (SRGAN)

Generate **S R G A N ** Image

## Instructions

1.Install:

```
pip install SuperResolution-GANs
```


2. Download Our Model
```python
import gdown
url = 'https://drive.google.com/uc?id=1MWDeLnpEaZDrKK-OjmzvYLxfjwp-GDcp'
output = 'generatoe_model.h5'
gdown.download(url, output, quiet=False)
```

3.Generate Super Resolution Image:
```python
from super_resolution_gans import srgan_utils
srgan_utils.SRGAN_predict(lr_image_path, model_path)
```


