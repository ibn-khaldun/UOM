# UOM


[![Build Status](https://travis-ci.com/Schlumberger/UOM.svg?token=qgnSxUFcykzzPyjostSM&branch=master)](https://travis-ci.com/Schlumberger/UOM)
[![CodeQL](https://github.com/Schlumberger/UOM/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/Schlumberger/UOM/actions/workflows/codeql-analysis.yml)
[![CircleCI](https://circleci.com/gh/Schlumberger/UOM/tree/master.svg?style=svg)](https://circleci.com/gh/Schlumberger/UOM/tree/master)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/Schlumberger/UOM/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/Schlumberger/UOM/?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/Schlumberger/UOM/badge.svg?branch=master)](https://coveralls.io/github/Schlumberger/UOM?branch=master)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/f2c1140afacf439c8fec00194acdc7db)](https://www.codacy.com/gh/Schlumberger/UOM/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Schlumberger/UOM&amp;utm_campaign=Badge_Grade)

# Build package

pip3 install wheel
python3 setup.py bdist_wheel

# Unit of Measure conversion tool

The conversion factors and unit symbols are based on the Energistics UOM 1.0:
https://www.energistics.org/energistics-unit-of-measure-standard/
extended with few extra unit aliases and "unitless" special unit that cannot be converted.

The units are case sensitives.


## Install
```
gsutil cp gs://slb_dl/whl/uom-0.4.0-py2.py3-none-any.whl .
pip install uom-0.4.0-py2.py3-none-any.whl
```

## Examples

Please find a few examples of possible utilization:

### Find conversion factors to be applied to convert from one unit to another

```
from uom import conversion_factors

scale, offset = conversion_factors(source='m', target='ft')
```
### Convert a value from one unit to another

```
from uom import convert_value

print(convert(value=10, source='m', target='ft'))
```
### Return the base (SI) unit and if you are using unit alias you can find the equivalent Energistics UOM symbol

```
from uom import base_unit, unit_alias

print(base_unit('kft.lbf'))
print(unit_alias('kft.lbf'))
```

If you have suggestions for improvement or you found bugs, please don't hesitate to put them in the issue list.