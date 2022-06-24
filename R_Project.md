# R Studio Project

For this project I used a public Diamonds dataset provided in R Studio.

## This simple bar chart shows the amount of Diamonds by Cut.

```{r}
data("diamonds")
qplot(cut, data=diamonds) +
  labs(y="Number of Diamonds", x="Cut", title="Quality of Cut")
```
![image](https://github.com/BeverlyFigueroa/Projects/blob/main/r_quality_of_cut.png?raw=true)

## This density line graph shows the amount of diamonds by Price.

```{r}
data("diamonds")
qplot(price, geom='density', data=diamonds) + 
  geom_density(fill='lightblue') +
  labs(x="Price", title="Density of Diamonds by Price")
```
![image](https://github.com/BeverlyFigueroa/Projects/blob/main/r_density.png?raw=true)

## Proportion of Color within each Cut.

```{r}
ggplot(diamonds, aes(cut)) +
  geom_bar(aes(fill=color)) + 
  theme(axis.text.x = element_text(angle=65, vjust=0.6)) +
  labs(title="Proportion of Color within Cut")
```
![image](https://github.com/BeverlyFigueroa/Projects/blob/main/r_proportion_color.png?raw=true)
