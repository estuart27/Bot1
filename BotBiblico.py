import telebot
import schedule
import time
from datetime import datetime
import threading
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random


print('Ativo ....')
# Substitua pelo token do seu bot
API_TOKEN = '7363677491:AAG5PYMSToyDvmiyDGJH1PCBNEefvAwNyoM'

chat_id = '6662355881'  # Substitua pelo ID do chat ou do usuário

bot = telebot.TeleBot(API_TOKEN)

ministracoes = [
    f"Lembre do seu propósito com dinheiro segundo a Bíblia:\nSustento pessoal\nSustento da Família\nSustento da obra de Deus\nCaridade",
    f"LEMBRE-SE:\nNão é sobre nós, mas sobre Jesus Cristo. Lembre que, quando você for direcionado a falar do Senhor, Ele já estará trabalhando nessa pessoa. Dê continuidade no que o Senhor já está fazendo, ELE JÁ ESTÁ FAZENDO.",
    f"FOCO - Dar a Deus o seu Tempo no dia a dia!\n1- Reserve um tempo no dia para estudo da palavra e oração.\n2- Reserve uma parte dos seus recursos para abençoar os necessitados.\n3- Reserve uma parte do seu talento e dom para servir seus irmãos (evangelismo, atenção, palavra, alegria, contribuir na igreja com seus dons).",
    f"Atos 7:59-60\nSe posicionar dói, se posicionar não traz elogios, mas críticas. É difícil se posicionar segundo o que o Senhor está falando e não o que a multidão está falando...",
    f"GUARDE SEU CORAÇÃO\nSeu coração é uma porta; tudo que você deixa entrar será guardado e externado para fora. A boca fala o que está cheio o coração. Então, guarde seu coração. Encha-o da palavra do Senhor.",
    f"Lucas 10:39-42 e Salmos 119:105 nos ensinam uma profunda verdade: a importância de aprender a desfrutar da presença do Senhor. Como Maria, que se assentou aos pés de Jesus para ouvir Suas palavras, precisamos acalmar nossa alma e silenciar os ruídos ao nosso redor. É na quietude diante Dele que encontramos direção para nossas vidas.\nEm vez de ficarmos ansiosos, buscando o que devemos fazer, somos chamados a contemplar Sua presença, a sentir Seu amor e cuidado. Quando desfrutamos da luz que Sua Palavra traz (Salmos 119:105), recebemos a verdadeira direção do céu para nossa caminhada. Só assim podemos vencer as lutas e encontrar o propósito que Deus tem para nós.",
    f"Autoridade: Seja exemplo para seus filhos\nA verdadeira autoridade não se impõe, mas se conquista através do exemplo. Como pais, somos chamados a liderar nossas famílias com amor, sabedoria e integridade. Nossos filhos aprendem mais com o que fazemos do que com o que falamos. Seja um modelo de comportamento, caráter e fé. Mostre-lhes como seguir a Deus e tomar decisões justas, para que eles vejam em você um reflexo daquilo que deseja que eles se tornem. Assim, sua autoridade será natural e respeitada, pois será fundamentada em ações que inspiram e transformam.",
    f"Deus escolheu o lugar e o tempo em que você está. Ele te levantou para esta geração, para este lugar e para este momento específico. Você está onde está porque Ele te preparou para cumprir um propósito único, no tempo certo, e no lugar certo.",
    f"Duas coisas que você precisa:\n1 - Tenha fé suficiente para ter paz e confiar em Deus\n 2 - Tenha fé suficiente para trabalhar para Cristo",
    f"Nao esqueça ,Coragem!, quem dá coragem é Deus",
    f"LEMBRE-SE\nQuem tem que dizer o que é bom pra minha vida é o Senhor.\nQuem tem que dizer o que é bom pra minha família é o Senhor\nQuem diz o que é melhor pro meu futuro é meu Senhor\nAssim diz o Senhor ...",


]

versiculos = [
    "Porque Deus amou o mundo de tal maneira que deu o seu Filho unigênito, para que todo aquele que nele crê não pereça, mas tenha a vida eterna." ,
    "Posso todas as coisas naquele que me fortalece." ,
    "O Senhor é o meu pastor; nada me faltará." ,
    "Entrega o teu caminho ao Senhor; confia nele, e ele o fará." ,
    "E sabemos que todas as coisas contribuem juntamente para o bem daqueles que amam a Deus, daqueles que são chamados segundo o seu propósito." ,
]

oracao = [
    # Oração por sabedoria
    "Senhor, concede-me sabedoria para tomar as decisões certas hoje e discernir a Tua vontade em todas as situações. Amém.",

    # Oração por proteção
    "Pai, guarda-me sob as Tuas asas de proteção. Que a Tua mão me proteja de todo o mal e que eu ande em segurança. Amém.",

    # Oração por força
    "Deus, quando me sinto fraco, renova minhas forças. Fortalece-me para enfrentar as batalhas e seguir com confiança. Amém.",

    # Oração por paz
    "Senhor, enche meu coração com a Tua paz que excede todo entendimento. Que eu possa descansar em Ti, independente das circunstâncias. Amém.",

    # Oração por cura
    "Deus, peço pela cura, seja física, emocional ou espiritual. Restaura o que está quebrado e traga saúde completa em minha vida. Amém."
]

mudar = ["Vocé precisa parar de falar alto","Precisa para de ser Ansioso","Preciso Valorizar mais minha familia",]

frases = [
    "O maior milagre que Deus pode fazer hoje é tomar um homem pecador e fazer dele um santo.",
    "Não é grande fé que tu precisas, mas fé em um grande Deus.",
    "A oração é a respiração vital da alma." ,
    "O que você faz com a Bíblia determina o que Deus fará com você." ,
    "Somente uma vida, que em breve passará; só o que é feito para Cristo durará.",
    "Se Cristo não for tudo para você, Ele não será nada para você." ,
    "Deus não escolhe pessoas capacitadas, Ele capacita os escolhidos." ,
    "Você nunca terá uma visão maior de Deus do que a que tem da Bíblia.",
    "Não há nada que satanás tema tanto como o cristão de joelhos." ,
    "O evangelho é apenas boas novas quando chega a tempo.",
]

sentimento = ["Quer um conselho - SE AME MAIS"]



sermoes = [
    {
        "titulo": "A Santidade de Deus",
        "texto_base": "Isaías 6:1-5",
        "mensagem": """
*Título:* A Santidade de Deus
*Texto base:* Isaías 6:1-5

*Pontos principais:*
1. *A natureza de Deus:* Deus é santo, totalmente separado do pecado. Devemos reconhecê-la em reverência.
2. *A resposta de Isaías:* Isaías, um profeta de Deus, reconheceu sua impureza ao ver a santidade de Deus.
3. *Nossa condição perante Deus:* Assim como Isaías, devemos reconhecer nossa condição pecaminosa diante de Deus.

*Conclusão:* Que possamos nos humilhar diante da santidade de Deus, reconhecer nossa necessidade de arrependimento e buscar continuamente Sua graça.
"""
    },
    {
        "titulo": "O Verdadeiro Arrependimento",
        "texto_base": "2 Coríntios 7:10",
        "mensagem": """
*Título:* O Verdadeiro Arrependimento
*Texto base:* 2 Coríntios 7:10

*Pontos principais:*
1. *Tristeza segundo Deus vs. Tristeza segundo o mundo:* A tristeza do mundo leva à morte, a tristeza segundo Deus leva à salvação.
2. *O coração endurecido:* Um coração endurecido sabe que está errado, mas não deseja mudar.
3. *O arrependimento genuíno:* O verdadeiro arrependimento é uma mudança interior profunda e resulta em uma transformação de vida.

*Conclusão:* Arrependimento é o chamado de Deus para todos nós. Hoje é o dia para humilhar-se diante do Senhor e clamar por transformação.
"""
    },
    {
        "titulo": "A Necessidade da Regeneração",
        "texto_base": "João 3:3-5",
        "mensagem": """
*Título:* A Necessidade da Regeneração
*Texto base:* João 3:3-5

*Pontos principais:*
1. *O que é o novo nascimento?* Não é uma mudança moral, mas uma obra sobrenatural do Espírito Santo.
2. *A depravação do homem:* Sem a regeneração, estamos mortos em nossos pecados.
3. *Os frutos da regeneração:* Uma vida transformada reflete os frutos do Espírito e o desejo de obedecer a Deus.

*Conclusão:* Examine a si mesmo. Você foi verdadeiramente regenerado? Busque a Deus, pois só Ele pode dar nova vida.
"""
    },
    {
        "titulo": "A Falsa Conversão",
        "texto_base": "Mateus 7:21-23",
        "mensagem": """
*Título:* A Falsa Conversão
*Texto base:* Mateus 7:21-23

*Pontos principais:*
1. *Muitos são enganados:* Muitos pensam ser salvos, mas nunca experimentaram a verdadeira regeneração.
2. *Sinais de uma falsa conversão:* O amor ao mundo e o pecado habitual são sinais de uma falsa conversão.
3. *O perigo da autojustificação:* Muitos confiam em suas obras ou afiliações religiosas em vez da fé genuína em Cristo.

*Conclusão:* Examine sua fé. Peça a Deus para revelar a verdade sobre sua condição espiritual e clame por Sua graça.
"""
    },
    {
        "titulo": "A Centralidade da Cruz",
        "texto_base": "1 Coríntios 1:18",
        "mensagem": """
*Título:* A Centralidade da Cruz
*Texto base:* 1 Coríntios 1:18

*Pontos principais:*
1. *O escândalo da cruz:* A cruz é vista como loucura para os que perecem, mas é o poder de Deus para os salvos.
2. *O sacrifício de Cristo:* Jesus suportou a ira de Deus em nosso lugar, pagando o preço pelos nossos pecados.
3. *A transformação através da cruz:* A cruz nos chama à rendição total, vivendo em obediência a Cristo.

*Conclusão:* A cruz de Cristo deve ser o centro de nossas vidas. Que possamos viver à luz do sacrifício de Jesus, sendo transformados por Seu amor.
"""
    },
    {
        "titulo": "O Caminho da Salvação",
        "texto_base": "Efésios 2:8",
        "mensagem": """
*Título:* O Caminho da Salvação
*Texto base:* Efésios 2:8

*Pontos principais:*
1. *A graça de Deus:* A salvação vem pela graça, não por obras. É um dom imerecido de Deus.
2. *A fé como meio:* Somos salvos pela fé, que nos conecta ao sacrifício de Cristo.
3. *O fruto da salvação:* A salvação resulta em boas obras, como um reflexo da transformação interior.

*Conclusão:* Não há nada que possamos fazer para ganhar a salvação. É pela fé e pela graça de Deus que somos transformados.
"""
    },
    {
        "titulo": "O Amor Perfeito",
        "texto_base": "1 João 4:18",
        "mensagem": """
*Título:* O Amor Perfeito
*Texto base:* 1 João 4:18

*Pontos principais:*
1. *A natureza do amor:* O amor de Deus é perfeito e lança fora todo medo.
2. *O relacionamento com Deus:* O amor verdadeiro surge de um relacionamento íntimo com Deus.
3. *Amor pelos outros:* Quem conhece o amor de Deus, deve refletir esse amor em suas relações com os outros.

*Conclusão:* Busquemos o amor perfeito de Deus, que transforma e nos capacita a amar sem medo.
"""
    },
    {
        "titulo": "A Santificação",
        "texto_base": "1 Tessalonicenses 4:3",
        "mensagem": """
*Título:* A Santificação
*Texto base:* 1 Tessalonicenses 4:3

*Pontos principais:*
1. *A vontade de Deus:* A santificação é a vontade de Deus para todos os crentes.
2. *O processo contínuo:* A santificação é um processo que acontece ao longo da vida.
3. *O papel do Espírito Santo:* O Espírito Santo nos capacita a viver em santidade e vencer o pecado.

*Conclusão:* Deus nos chama à santificação. Devemos nos render ao Espírito Santo, que nos transforma continuamente.
"""
    },
    {
        "titulo": "A Lei e o Evangelho",
        "texto_base": "Romanos 3:31",
        "mensagem": """
*Título:* A Lei e o Evangelho
*Texto base:* Romanos 3:31

*Pontos principais:*
1. *A função da lei:* A lei de Deus nos mostra nosso pecado e nossa necessidade de um Salvador.
2. *A graça do evangelho:* O evangelho é a boa notícia de que Jesus cumpriu a lei em nosso lugar.
3. *Viver em obediência:* Embora não sejamos salvos pela lei, somos chamados a viver em obediência como resposta à graça.

*Conclusão:* A lei e o evangelho trabalham juntos para nos trazer à salvação e nos guiar em uma vida de obediência a Deus.
"""
    },
    {
        "titulo": "A Verdadeira Conversão",
        "texto_base": "Mateus 7:13-14",
        "mensagem": """
*Título:* A Verdadeira Conversão
*Texto base:* Mateus 7:13-14

*Pontos principais:*
1. *O caminho estreito:* A verdadeira conversão nos coloca no caminho estreito que leva à vida eterna.
2. *Frutos de arrependimento:* A verdadeira conversão é evidenciada por uma mudança de vida e frutos de arrependimento.
3. *O chamado ao discipulado:* Seguir a Cristo exige sacrifício e renúncia ao mundo.

*Conclusão:* Examine sua vida. Você está no caminho estreito? A verdadeira conversão é demonstrada por uma vida transformada em Cristo.
"""
    },

    # Sermões de Jonathan Edwards
    {
        "titulo": "Pecadores nas Mãos de um Deus Irado",
        "texto_base": "Deuteronômio 32:35",
        "mensagem": """
*Título:* Pecadores nas Mãos de um Deus Irado
*Texto base:* Deuteronômio 32:35

*Pontos principais:*
1. *A justiça de Deus:* Deus é justo em sua ira contra o pecado.
2. *O perigo da condenação:* Sem arrependimento, os pecadores estão a um passo da destruição eterna.
3. *A misericórdia de Deus:* Deus oferece misericórdia por meio de Jesus Cristo, mas o tempo para arrependimento é limitado.

*Conclusão:* Fuja da ira vindoura e corra para a graça de Deus em Jesus Cristo antes que seja tarde demais.
"""
    },
    {
        "titulo": "A Beleza da Santidade",
        "texto_base": "Salmo 29:2",
        "mensagem": """
*Título:* A Beleza da Santidade
*Texto base:* Salmo 29:2

*Pontos principais:*
1. *O caráter santo de Deus:* A santidade de Deus é bela e perfeita.
2. *O chamado à santidade:* Somos chamados a refletir a santidade de Deus em nossas vidas.
3. *A alegria na santidade:* Há verdadeira alegria e paz em viver uma vida de santidade diante de Deus.

*Conclusão:* Que possamos buscar a santidade em nossas vidas, encontrando beleza e alegria em ser conformados à imagem de Cristo.
"""
    },
    {
        "titulo": "A Soberania de Deus",
        "texto_base": "Efésios 1:11",
        "mensagem": """
*Título:* A Soberania de Deus
*Texto base:* Efésios 1:11

*Pontos principais:*
1. *Deus controla todas as coisas:* Nada acontece fora do controle soberano de Deus.
2. *Confiança na soberania:* Podemos confiar que Deus está no controle, mesmo em tempos de dificuldade.
3. *Responsabilidade humana:* A soberania de Deus não anula nossa responsabilidade de viver em obediência e fé.

*Conclusão:* A soberania de Deus nos dá paz e confiança, sabendo que Ele está no controle de tudo.
"""
    },
    {
        "titulo": "O Amor de Deus por Seu Povo",
        "texto_base": "João 3:16",
        "mensagem": """
*Título:* O Amor de Deus por Seu Povo
*Texto base:* João 3:16

*Pontos principais:*
1. *Deus amou o mundo:* O amor de Deus é demonstrado na oferta de Seu Filho para a salvação.
2. *Amor sacrificial:* O amor de Deus é um amor sacrificial, que entregou Jesus para nos resgatar.
3. *Amor transformador:* O amor de Deus transforma nossas vidas, nos chamando a amar como Ele ama.

*Conclusão:* Somos chamados a responder ao amor de Deus com fé e obediência, e a demonstrar esse amor em nossas vidas diárias.
"""
    },
    {
        "titulo": "A Glória de Deus",
        "texto_base": "1 Coríntios 10:31",
        "mensagem": """
*Título:* A Glória de Deus
*Texto base:* 1 Coríntios 10:31

*Pontos principais:*
1. *O propósito da vida:* Tudo o que fazemos deve ser para a glória de Deus.
2. *A glória de Deus na criação:* Deus é glorificado em toda a criação, e somos chamados a refletir essa glória.
3. *A busca pela glória de Deus:* Devemos viver nossas vidas de maneira que glorifique a Deus em todos os aspectos.

*Conclusão:* Que possamos viver para a glória de Deus, buscando refletir Sua grandeza em todas as nossas ações e decisões.
"""
    }
]


def criar_menu_opcoes():
    # Cria o menu com botões
    markup = InlineKeyboardMarkup()
    
    # Adicionar botões com as opções desejadas
    markup.row_width = 2  # Define quantos botões por linha
    markup.add(InlineKeyboardButton("Adicionar Ministração", callback_data="ministracao"),
               InlineKeyboardButton("Adicionar Versículo Bíblico", callback_data="versiculo"),
               InlineKeyboardButton("Adicionar Necessidade de Mudar", callback_data="necessidade"),
               InlineKeyboardButton("Pedido de Oração", callback_data="pedido_oracao"),
               InlineKeyboardButton("Frases de Pastores e Teólogos", callback_data="frases"),
               InlineKeyboardButton("Sentimento do Dia", callback_data="sentimento"),
               InlineKeyboardButton("Escrever o que está sentindo", callback_data="escrever_sentimento"))
    
    return markup

# Comando /start que envia o menu com as opções
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "O que o Senhor tem ministrado em seu coração ?", reply_markup=criar_menu_opcoes())


# Função para lidar com as respostas dos botões
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "ministracao":
        bot.send_message(call.message.chat.id, "Escreva sua ministração:")
        bot.register_next_step_handler(call.message, salvar_ministracao)
    elif call.data == "versiculo":
        bot.send_message(call.message.chat.id, "Escreva o versículo:")
        bot.register_next_step_handler(call.message, salvar_versiculo)

    elif call.data == "necessidade":
        bot.send_message(call.message.chat.id, "Escreva sua Necessidade de Mudar?")
        bot.register_next_step_handler(call.message, salvar_mudar)

    elif call.data == "pedido_oracao":
        bot.send_message(call.message.chat.id, "Escreva seu pedido de oração:")
        bot.register_next_step_handler(call.message, salvar_oracao)

    elif call.data == "frases":
        bot.send_message(call.message.chat.id, "Adicione uma frase:")
        bot.register_next_step_handler(call.message, salvar_frases)

    elif call.data == "sentimento":
        bot.send_message(call.message.chat.id, "Qual seu sentimento de hoje?")
        bot.register_next_step_handler(call.message, salvar_sentimento)

    elif call.data == "escrever_sentimento":
        bot.send_message(call.message.chat.id, "Você escolheu 'Escrever o que está sentindo'. Escreva seus sentimentos:")
        print(ministracoes)
        print(mudar)
        print(oracao)
        print(frases)
        print(sentimento)
        print(versiculos)


#============================== FINALIZADO =================================================================


def salvar_ministracao(message):
    user_id = message.from_user.id
    ministracao = message.text  # Captura o texto da ministração
    
    # Salva a ministração na variável (ou banco de dados)
    ministracoes.append(ministracao)
    
    # Confirmação ao usuário
    bot.send_message(message.chat.id, "Sua ministração foi salva com sucesso!")


def salvar_versiculo(message):
    user_id = message.from_user.id
    ministracao = message.text  # Captura o texto da ministração
    
    # Salva a ministração na variável (ou banco de dados)
    versiculos.append(ministracao)
    
    # Confirmação ao usuário
    bot.send_message(message.chat.id, "Seu versiculo foi salva com sucesso!")


def salvar_oracao(message):
    user_id = message.from_user.id
    ministracao = message.text  # Captura o texto da ministração
    
    # Salva a ministração na variável (ou banco de dados)
    oracao.append(ministracao)

    # Confirmação ao usuário
    bot.send_message(message.chat.id, "Sua oração foi salva com sucesso!")


def salvar_mudar(message):
    user_id = message.from_user.id
    ministracao = message.text  # Captura o texto da ministração
    
    # Salva a ministração na variável (ou banco de dados)
    mudar.append(ministracao)
    
    # Confirmação ao usuário
    bot.send_message(message.chat.id, "o que você precisa mudar foi salva com sucesso!")


def salvar_frases(message):
    user_id = message.from_user.id
    ministracao = message.text  # Captura o texto da ministração
    
    # Salva a ministração na variável (ou banco de dados)
    frases.append(ministracao)
    
    # Confirmação ao usuário
    bot.send_message(message.chat.id, "Frase do dia foi salva com sucesso!")


def salvar_sermao(message):
    user_id = message.from_user.id
    ministracao = message.text  # Captura o texto da ministração
    
    # Salva a ministração na variável (ou banco de dados)
    sermoes.append(ministracao)
    
    # Confirmação ao usuário
    bot.send_message(message.chat.id, "Sermão foi salva com sucesso!")

def salvar_sentimento(message):
    user_id = message.from_user.id
    ministracao = message.text  # Captura o texto da ministração
    
    # Salva a ministração na variável (ou banco de dados)
    sentimento.append(ministracao)
    
    # Confirmação ao usuário
    bot.send_message(message.chat.id, "Seu sentimento do dia foi salva com sucesso!")

#===============================================================================================

# Comando /help
@bot.message_handler(commands=['Jesus'])
def send_help(message):
    sermao = random.choice(sermoes)["mensagem"]
    # bot.send_message(chat_id=chat_id, text=sermao, parse_mode='Markdown')
    bot.reply_to(message, text=sermao, parse_mode='Markdown')



@bot.message_handler(commands=['quantidade'])
def quantidade_versos(message):
    bot.reply_to(message, f">> LISTAS DE CONTEÚDOS <<\nMinistrações - [{len(ministracoes)}]\nVersos Bíblicos - [{len(versiculos)}]\nOração - [{len(oracao)}]\nHábitos para mudar - [{len(mudar)}]\nFrases - [{len(frases)}]\nSentimentos - [{len(sentimento)}]\nSermão - [{len(sermoes)}]")



@bot.message_handler(commands=['Excluir'])
def exluindo_msg(message):
    bot.send_message(message.chat.id, "Escolha uma lista para modificar (oracao, ministracao, versiculo, frases , mudar , sentimento):")

    # Espera a próxima mensagem do usuário com o nome da lista
    bot.register_next_step_handler(message, escolher_lista)

def escolher_lista(message):
    user_id = message.from_user.id
    lista_nome = message.text.strip().lower()  # Captura o nome da lista enviada e converte para minúsculas
    
    # Verifica qual lista o usuário quer modificar
    if lista_nome == "oracao":
        lista = oracao
    elif lista_nome == "ministracao":
        lista = ministracoes
    elif lista_nome == "versiculo":
        lista = versiculos
    elif lista_nome == 'frases':
        lista = frases
    elif lista_nome == 'mudar':
        lista = mudar
    elif lista_nome == 'sentimento':
        lista = sentimento
    elif lista_nome == 'sermao':
        lista = sermoes
    else:
        bot.send_message(message.chat.id, "Nome de lista inválido. Tente novamente.")
        return  # Se o nome da lista for inválido, para o processo
    
    # Verifica se a lista está vazia
    if not lista:
        bot.send_message(message.chat.id, f"A lista '{lista_nome}' está vazia.")
        return
    
    # Pergunta qual item remover
    bot.send_message(message.chat.id, "Qual índice você gostaria de remover (começa em 0)?")

    # Espera o próximo passo para pegar o índice e apagar o item da lista escolhida
    bot.register_next_step_handler(message, apagar_item, lista)

def apagar_item(message, lista):
    try:
        indice = int(message.text)  # Pega o índice informado pelo usuário
        item_removido = lista.pop(indice)  # Remove o item da lista
        bot.send_message(message.chat.id, f"Item '{item_removido}' foi removido com sucesso.")
    except (IndexError, ValueError):
        bot.send_message(message.chat.id, "Índice inválido. Por favor, tente novamente.")

    # Exibe a lista atualizada
    # bot.send_message(message.chat.id, f"Lista atualizada: {', '.join(lista) if lista else 'vazia'}")
    bot.send_message(message.chat.id, f"Lista atualiza com sucesso")



# Função para enviar mensagem agendada
def enviar_mensagem():
    listas = [ministracoes, versiculos, oracao , sermoes , frases ]

    lista_selecionada = random.choice(listas)
    
    if lista_selecionada:
        mensagem = random.choice(lista_selecionada)
    else:
        mensagem = "Lista está vazia."

    bot.send_message(chat_id, mensagem)
    print(f"Mensagem enviada às {datetime.now().strftime('%H:%M:%S')}")


def agendar_mensagens():
    schedule.every().day.at("07:40").do(enviar_mensagem)
    schedule.every().day.at("16:00").do(enviar_mensagem)
    schedule.every().day.at("19:45").do(enviar_mensagem)
    schedule.every().day.at("00:00").do(enviar_mensagem)


    while True:
        schedule.run_pending()  # Verifica se há tarefas agendadas para executar
        time.sleep(1)  # Aguardar 1 segundo antes de verificar novamente


def iniciar_bot_e_agendamento():
    # Cria uma nova thread para o agendamento
    agendamento_thread = threading.Thread(target=agendar_mensagens)
    agendamento_thread.start()

    # Inicia o bot para receber mensagens
    bot.infinity_polling()

# Iniciar o bot e o agendamento juntos
if __name__ == '__main__':
    iniciar_bot_e_agendamento()
