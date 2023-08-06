# cloudML PYtorch Assistant

## Install
```bash
pip install cloudml-pytorch-assistant -i https://pkgs.d.xiaomi.net/artifactory/api/pypi/pypi-release-virtual/simple
```

## Usage
### using adrn dataloader
only support resource: "data-file"    
```python
from cloudml import get_res_from_adrn

adrn = "adrn::data-file:c5:676:image-net::1:/root/total-annotation.xml"
total_xml = get_res_from_adrn(adrn)
```

### using ThetisDataSet
only support resource:"data-set".    
ThetisDataSet is a subclass of [DataSet](https://pytorch.org/tutorials/beginner/basics/data_tutorial.html#creating-a-custom-dataset-for-your-files)

```python
from cloudml import ThetisDataSet

# Create dataset from adrn
train_ds_adrn = "adrn::data-set:c5:676:image-net-train::1"
training_data = ThetisDataSet(train_ds_adrn, None)

test_ds_adrn = "adrn::data-set:c5:676:image-net-test::1"
test_data = ThetisDataSet(test_ds_adrn, None)

# Create data loaders.
train_dataloader = DataLoader(training_data, batch_size=batch_size)
test_dataloader = DataLoader(test_data, batch_size=batch_size)

```

## What is adrn?
https://xiaomi.f.mioffice.cn/docs/dock4jW3DFkwRaQC3KZKVZ27KNd