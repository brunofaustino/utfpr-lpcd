# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 13:45:05 2021

@author: bfaam
"""

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

class DataBase():
    
    def __init__(self, dbname='postgres', user='postgres', password='Postgres2019!', statement_tables=None):
        self.user = user
        self.password = password
        self.statement_tables = statement_tables
        self.dbname = dbname
        
    def set_connection(self, dbname='postgres'):
        #self.conn = psycopg2.connect("dbname={} user={} password={}".format(dbname, self.user, self.password))
        self.conn = psycopg2.connect("user={} password={} port=15432".format(self.user, self.password))
        self.conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        self.cursor = self.conn.cursor()
        
    def create_tables(self, statement_tables):
        self.create_database()
        for stm in statement_tables:
            self.cursor.execute("DROP TABLE IF EXISTS {} CASCADE;".format(stm['table_name']))
            self.cursor.execute(stm['create_table'])
        print('OK. Tabelas criadas com sucesso.')
        self.close_connection()
            
    def create_database(self):
        self.set_connection()
        try:
            self.cursor.execute('DROP DATABASE IF EXISTS {};'.format(self.dbname))
            self.cursor.execute('CREATE DATABASE {};'.format(self.dbname))
        except Exception as ex:
            print('Aviso: falha ao recriar o database, provavelmente já existente.')
        self.set_connection(self.dbname)
        
    def close_connection(self):
        self.cursor.close()
        self.cursor.close()

TABLE_CASOS_COVID = "casos_covid"
TABLE_LOCALIZACAO = "localizacao"

CREATE_CASOS_COVID = {
        "table_name": TABLE_CASOS_COVID,
        "create_table": "CREATE TABLE {} (" \
              "idcasos_covid INT PRIMARY KEY," \
              "date VARCHAR(45) NULL," \
              "epidemiological_week INT NULL," \
              "casos_covidcol VARCHAR(45) NULL," \
              "is_last INT NULL," \
              "is_repeated INT NULL," \
              "last_available_confirmed INT NULL," \
              "last_available_confirmed_per_100k_inhabitants NUMERIC(10,2) NULL," \
              "last_available_death_rate VARCHAR(45) NULL," \
              "last_available_deaths VARCHAR(45) NULL," \
              "new_confirmed INT NULL," \
              "new_deaths INT NULL" \
        ")".format(TABLE_CASOS_COVID)
        }
CREATE_LOCALIZACAO = {
        "table_name": TABLE_LOCALIZACAO,
        "create_table": "CREATE TABLE {}(" \
              "city VARCHAR(45) NULL," \
              "city_ibge_code VARCHAR(45) NULL," \
              "estimated_population_2019 INT NULL," \
              "order_for_place VARCHAR(45) NULL," \
              "place_type VARCHAR(45) NULL," \
              "state VARCHAR(45) NULL," \
              "casos_covid_idcasos_covid INT NOT NULL," \
              "CONSTRAINT fk_localização_casos_covid" \
              "  FOREIGN KEY (casos_covid_idcasos_covid)" \
              "  REFERENCES casos_covid (idcasos_covid)" \
            ")".format(TABLE_LOCALIZACAO)
        }

statement_tables = [CREATE_CASOS_COVID, CREATE_LOCALIZACAO]

DATABASE = 'grupo_z'
dataBase = DataBase(dbname=DATABASE)
dataBase.create_tables(statement_tables)