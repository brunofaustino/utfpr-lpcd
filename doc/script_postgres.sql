CREATE TABLE IF NOT EXISTS casos_covid (
  idcasos_covid INT PRIMARY KEY,
  date VARCHAR(45) NULL,
  epidemiological_week INT NULL,
  casos_covidcol VARCHAR(45) NULL,
  is_last INT NULL,
  is_repeated INT NULL,
  last_available_confirmed INT NULL,
  last_available_confirmed_per_100k_inhabitants NUMERIC(10,2) NULL,
  last_available_death_rate VARCHAR(45) NULL,
  last_available_deaths VARCHAR(45) NULL,
  new_confirmed INT NULL,
  new_deaths INT NULL
)

CREATE TABLE IF NOT EXISTS localizacao (
  city VARCHAR(45) NULL,
  city_ibge_code VARCHAR(45) NULL,
  estimated_population_2019 INT NULL,
  order_for_place VARCHAR(45) NULL,
  place_type VARCHAR(45) NULL,
  state VARCHAR(45) NULL,
  casos_covid_idcasos_covid INT NOT NULL,
  CONSTRAINT fk_localização_casos_covid
    FOREIGN KEY (casos_covid_idcasos_covid)
    REFERENCES casos_covid (idcasos_covid)
)

drop table localizacao;
drop table casos_covid;

select * from casos_covid;
select * from localizacao;




































