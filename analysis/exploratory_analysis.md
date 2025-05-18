# Exploratory Analysis on Seasonal Trends in Product Sales vs Weather

## Insights

![Sales by Month](../images/prod_cat_sales_by_month.png)

![Sales by Season](../images/sales_bar_chart.png)

## Correlation Metrics against Quantity Sold for each Product Category

### Melbourne

#### Season: Summer

| Product Category | Temperature | Humidity  | Wind Speed |
| ---------------- | ----------- | --------- | ---------- |
| Cold and Flu     | -0.017184   | 0.055204  | -0.094826  |
| Hayfever         | 0.123537    | -0.092868 | 0.086630   |
| Hair Care        | -0.254682   | 0.301150  | -0.108640  |
| Cosmetics        | -0.110918   | 0.209303  | -0.065083  |

#### Season: Autumn

| Product Category | Temperature | Humidity  | Wind Speed |
| ---------------- | ----------- | --------- | ---------- |
| Cold and Flu     | -0.322971   | 0.166929  | 0.109741   |
| Hayfever         | 0.103816    | -0.009444 | 0.104045   |
| Hair Care        | -0.224930   | -0.044986 | 0.231045   |
| Cosmetics        | -0.427746   | 0.223014  | 0.250944   |

#### Season: Winter

| Product Category | Temperature | Humidity  | Wind Speed |
| ---------------- | ----------- | --------- | ---------- |
| Cold and Flu     | -0.175755   | 0.055498  | 0.121477   |
| Hayfever         | 0.030186    | 0.056757  | -0.030300  |
| Hair Care        | -0.216425   | -0.095032 | -0.018897  |
| Cosmetics        | -0.293593   | 0.165340  | 0.081963   |

#### Season: Spring

| Product Category | Temperature | Humidity  | Wind Speed |
| ---------------- | ----------- | --------- | ---------- |
| Cold and Flu     | 0.118805    | 0.121417  | -0.042001  |
| Hayfever         | -0.050652   | -0.105227 | 0.044570   |
| Hair Care        | -0.019799   | -0.002617 | -0.190022  |
| Cosmetics        | 0.228933    | 0.069709  | -0.069956  |


### Sydney

#### Season: Summer

| Product Category | Temperature | Humidity  | Wind Speed |
| ---------------- | ----------- | --------- | ---------- |
| Cold and Flu     | -0.100630   | -0.000355 | -0.165889  |
| Hayfever         | -0.051660   | 0.117467  | -0.067575  |
| Hair Care        | 0.123258    | 0.007074  | -0.236000  |
| Cosmetics        | 0.096155    | -0.034411 | -0.259721  |


### Season: Autumn

| Product Category | Temperature | Humidity  | Wind Speed |
| ---------------- | ----------- | --------- | ---------- |
| Cold and Flu     | -0.427768   | 0.009132  | -0.075551  |
| Hayfever         | 0.147855    | -0.017894 | -0.009876  |
| Hair Care        | -0.424450   | 0.044381  | 0.077581   |
| Cosmetics        | -0.420834   | -0.137068 | 0.183937   |


#### Season: Winter

| Product Category | Temperature | Humidity  | Wind Speed |
| ---------------- | ----------- | --------- | ---------- |
| Cold and Flu     | -0.217438   | -0.024273 | 0.148838   |
| Hayfever         | 0.131037    | -0.000950 | -0.036004  |
| Hair Care        | -0.145061   | 0.013104  | 0.021535   |
| Cosmetics        | -0.051653   | 0.006147  | 0.098868   |


#### Season: Spring

| Product Category | Temperature | Humidity  | Wind Speed |
| ---------------- | ----------- | --------- | ---------- |
| Cold and Flu     | -0.005907   | 0.125050  | -0.046885  |
| Hayfever         | -0.063298   | -0.320177 | -0.141975  |
| Hair Care        | -0.094458   | -0.283150 | -0.287497  |
| Cosmetics        | 0.031483    | 0.215109  | -0.106779  |

## Seasonal Insights on Product Sales

1. There is a negative correlation between Cold and Flu product sales and temperature during Autumn and Winter. This indicates that cooler temperatures coincide with increased demand for these products, which is line with typical flu seasonality. The correlation is much lower during warmer seasons such as Spring and Summer, which is also reflected by the lower sales numbers.

2. There is a positive correlation between Hair Care product sales and humidity during Summer. This suggests that increased humidity may drive higher demand for hair care products, possibly due to higher probability of hair frizz or damage. This pattern is less pronounced or negative in other seasons, highlighting it is a seasonal effect.

3. There is a consistent strong negative correlation with Cosmetics and temperature in autumn and winter months for both Melbourne and Sydney. This reflects that the lowering of temperature may drive higher cosmetic purchase to meet skincare needs, when it is drier and cooler. This then turns into a positive correlation for Spring months, suggesting customers are buying more cosmetics as the weather warms up.
