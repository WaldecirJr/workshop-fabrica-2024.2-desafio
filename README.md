**** Colsuta metereólogica para viagens ****


** Repositório criado para o desafio da fábrica de software 2024.2 **

Descrição do ConsultaMET

Visão Geral
O ConsultaMET é uma aplicação web desenvolvida com Django e Django Rest Framework que permite aos usuários planejar e gerenciar suas viagens de forma eficiente. O aplicativo oferece funcionalidades para obter dados atualizados sobre as condições climáticas dos locais planejados. Além disso, o ConsultaMET integra-se com APIs externas para fornecer informações adicionais e enriquecer a experiência do usuário.

Funcionalidades Principais

1. Gestão de Itinerários:

Criação e Edição: Os usuários podem criar novos itinerários, incluindo detalhes como nome, descrição, data de início e fim. É possível adicionar, editar e remover destinos para cada itinerário.
Visualização de Destinos: Cada itinerário pode conter múltiplos destinos. Os usuários podem visualizar e gerenciar os destinos associados a um itinerário específico.

2. CRUD Completo para Entidades:

O aplicativo gerencia duas entidades principais:

2.1. Itinerários: Contém informações sobre a viagem, incluindo datas e uma lista de destinos.
2.2. Condições climáticas: Contém informações sobre as condições climáticas da viagem.
2.3. Operações CRUD: Os usuários podem criar, ler, atualizar e excluir itinerários e destinos usando uma interface intuitiva.

3. Integração com API Externa de Clima:

Dados Climáticos: O ConsultaMET consome uma API gratuita de previsão do tempo (OpenWeatherMap) para obter dados climáticos atualizados para cada destino.
Armazenamento de Dados: As informações sobre temperatura e condições climáticas são armazenadas no banco de dados, permitindo que os usuários visualizem as condições esperadas durante sua viagem.

Backend: Django, Django Rest Framework
Banco de Dados: PostgreSQL (ou outro banco de dados relacional suportado pelo Django)
APIs de Clima: OpenWeatherMap
