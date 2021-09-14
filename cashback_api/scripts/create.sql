-- -----------------------------------------------------
-- DROP TABLES
-- -----------------------------------------------------
DROP TABLE IF EXISTS public.CREDITO CASCADE;
DROP TABLE IF EXISTS public.REVENDEDOR CASCADE;
DROP TABLE IF EXISTS public.COMPRA CASCADE;
-- -----------------------------------------------------
-- Table public.REVENDEDOR
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS public.REVENDEDOR (
  ID_REVENDEDOR SERIAL PRIMARY KEY,
  NOME VARCHAR(160) NOT NULL,
  CPF VARCHAR(200) NOT NULL UNIQUE,
  EMAIL VARCHAR(200) NOT NULL,
  SENHA VARCHAR(300) NOT NULL
);
CREATE INDEX CPF_INDEX ON public.REVENDEDOR (CPF);
-- -----------------------------------------------------
-- Table public.CREDITO
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS public.CREDITO (
  ID_CREDITO SERIAL PRIMARY KEY,
  PORCENTAGEM FLOAT NOT NULL,
  ATIVO BOOLEAN NOT NULL
);
-- -----------------------------------------------------
-- Table public.COMPRA
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS public.COMPRA (
  CODIGO VARCHAR(45) PRIMARY KEY,
  VALOR DECIMAL(10, 2) NOT NULL,
  DATA TIMESTAMP NOT NULL,
  FK_REVENDEDOR_ID_REVENDEDOR INT NOT NULL,
  FK_CREDITO_ID_CREDITO INT NOT NULL,
  CONSTRAINT fk_COMPRA_REVENDEDOR
    FOREIGN KEY (FK_REVENDEDOR_ID_REVENDEDOR)
    REFERENCES public.REVENDEDOR (ID_REVENDEDOR)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT fk_CREDITO_ID_CREDITO
  FOREIGN KEY (FK_CREDITO_ID_CREDITO)
  REFERENCES public.CREDITO (ID_CREDITO)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION
);
-- -----------------------------------------------------
-- INSERT CREDITO
-- -----------------------------------------------------
INSERT INTO public.CREDITO (PORCENTAGEM, ATIVO)
VALUES (0.10, TRUE),
  (0.15, TRUE),
  (0.20, TRUE);