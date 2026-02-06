-- SQL usado na SUPABASE para criar a tabela

CREATE TABLE IF NOT EXISTS public.cotacoes (
  id BIGSERIAL PRIMARY KEY, -- BIGSERIAL(cria um inteiro grande(8bytes)) PRIMARY KEY(ID único linha-a-linha)
  ativo TEXT NOT NULL, -- [Ex.: BTC-USD, GC=F, CL=F, SI=F] TEXT(string de tamanho variável) NOT NULL(n pode ser vazia, é obrigatório estar preenchida)
  preco NUMERIC(18,6) NOT NULL, -- [Preço coletado] NOT NULL(n pode ser vazia, é obrigatório estar preenchida) NUMERIC(18 digitos, 6 casas decimais)
  moeda CHAR(3) NOT NULL DEFAULT 'USD', -- NOT NULL(n pode ser vazia, é obrigatório estar preenchida) CHAR(aceita 3 caracteres apenas) DEFAULT(Se n informado, retorna USD)
  horario_coleta TIMESTAMPTZ NOT NULL, -- [Quando o script coletou] NOT NULL(n pode ser vazia, é obrigatório estar preenchida) TIMESTAMPTZ(hora com fuso horario)
  inserido_em TIMESTAMPTZ NOT NULL DEFAULT NOW() -- NOT NULL(n pode ser vazia, é obrigatório estar preenchida) TIMESTAMPTZ(hora com fuso horario) DEFAULT NOW(Se n houver valor, retorna a hora atual)
);