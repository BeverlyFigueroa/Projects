# SQL Project

This is my SQL work with data from the Coronavirus (COVID-19) Deaths dataset from Our World In Data (http://https://ourworldindata.org/covid-deaths).


## I first take a look at the data as a whole. 
_I am working with 2 different files: Covid_Deaths and Covid_Vaccinations:_

- Covid_Deaths
```{sql connection=}
SELECT *
FROM `stoked-monitor-351301.Covid_Project.Covid_Deaths`
```
![image](https://github.com/BeverlyFigueroa/Projects/blob/main/sql_Capture_1.PNG?raw=true)

- Covid_Vaccinations
```{sql connection=}
SELECT *
FROM `stoked-monitor-351301.Covid_Project.Covid_Vaccinations
```
![image](https://github.com/BeverlyFigueroa/Projects/blob/main/sql_Capture_2.PNG?raw=true)

## Next, I will select the data I will use. <br>
_I use the WHERE command to screen out data by region, as I only want to look at countries:_
```{sql connection=}
SELECT 
  location, date, total_cases,new_cases, total_deaths, population
FROM `stoked-monitor-351301.Covid_Project.Covid_Deaths`
WHERE continent IS NOT NULL
ORDER BY 1,2
```
![image](https://github.com/BeverlyFigueroa/Projects/blob/main/sql_Capture_3.PNG?raw=true)


## Here I am looking at Total Cases vs Total Deaths.<br>
_This query shows the likelihood of dying if you contract COVID in your country:_
```{sql connection=}
SELECT
  location, date, total_cases,total_deaths, 
  (total_deaths/total_cases)*100 AS Death_Percentage
FROM `stoked-monitor-351301.Covid_Project.Covid_Deaths`
WHERE continent is not null
ORDER BY 1,2 DESC
```
![image](https://github.com/BeverlyFigueroa/Projects/blob/main/sql_Capture_4.PNG?raw=true)


## Here we are looking at the Total Cases vs Population<br>
_This query shows what percentage of the population got Covid in China (just as an example):_
```{sql connection=}
SELECT
  location, date, population, total_cases, 
  FORMAT('%s%%', CAST(ROUND((total_cases/population)*100, 2) AS STRING)) AS Population_Infected_Percentage
FROM `stoked-monitor-351301.Covid_Project.Covid_Deaths`
WHERE continent IS NOT NULL
AND location = 'China'
ORDER BY 1,2
```
![image](https://github.com/BeverlyFigueroa/Projects/blob/main/sql_Capture_5.PNG?raw=true)


## Here I am looking at Countries with the Highest Infection Rate, compared to the Population:
```{sql connection=}
SELECT 
  location, population, MAX(total_cases) AS Highest_Infection_Rate, 
  ROUND((MAX(total_cases/population)*100), 2) AS Population_Infected_Percentage
FROM `stoked-monitor-351301.Covid_Project.Covid_Deaths`
WHERE continent IS NOT NULL
GROUP BY location, population
ORDER BY Population_Infected_Percentage DESC
```
![image](https://github.com/BeverlyFigueroa/Projects/blob/main/sql_Capture_6.PNG?raw=true)


## This is showing Countries with the Highest Death Count per Population:
```{sql connection=}
SELECT
  location, MAX(CAST(total_deaths AS int)) AS Total_Death_Count
FROM `stoked-monitor-351301.Covid_Project.Covid_Deaths`
WHERE continent IS NOT NULL
GROUP BY location
ORDER BY Total_Death_Count DESC
```
![image](https://github.com/BeverlyFigueroa/Projects/blob/main/sql_Capture_7.PNG?raw=true)


## Now we can break it down by Continent<br>
_This query shows the Continents with Highest Death Count per Population:_
```{sql connection=}
SELECT
  continent, MAX(CAST(total_deaths AS int)) AS Total_Death_Count
FROM `stoked-monitor-351301.Covid_Project.Covid_Deaths`
WHERE continent IS NOT NULL
GROUP BY continent
ORDER BY Total_Death_Count DESC
```
![image](https://github.com/BeverlyFigueroa/Projects/blob/main/sql_Capture_8.PNG?raw=true)


## We can also look at the Global Numbers
```{sql connection=}
SELECT
  SUM(new_cases) AS Total_Cases, 
  SUM(CAST(new_deaths AS int)) AS Total_Deaths,
  ROUND((SUM(CAST(new_deaths AS int))/SUM(new_cases)*100), 2) AS Global_Death_Percentage
FROM `stoked-monitor-351301.Covid_Project.Covid_Deaths`
WHERE continent IS NOT NULL
```
![image](https://github.com/BeverlyFigueroa/Projects/blob/main/sql_Capture_9.PNG?raw=true)


## I will now Join my two datasets (Covid_Deaths and Covid_Vaccinations)<br>
_We are using a rolling count that increases day by day to look at Total Population vs Vaccinations per day:_
```{sql connection=}
SELECT dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations,
  SUM(CAST(vac.new_vaccinations as int)) OVER (PARTITION BY dea.location ORDER BY dea.location, dea.date) 
  AS Rolling_People_Vaccinated
FROM `stoked-monitor-351301.Covid_Project.Covid_Deaths` dea
JOIN `stoked-monitor-351301.Covid_Project.Covid_Vaccinations` vac
  ON dea.location = vac.location
  AND dea.date = vac.date
WHERE dea.continent IS NOT NULL
ORDER BY 3
```
![image](https://github.com/BeverlyFigueroa/Projects/blob/main/sql_Capture_10.PNG?raw=true)