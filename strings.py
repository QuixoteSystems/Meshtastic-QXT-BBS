'''
All the string to change in the language you want
'''

###############
# CONFIG_INIT #
###############

#SYNC_BBS_NODES = "Configured to sync with the following BBS nodes: "
SYNC_BBS_NODES = "Nodos BBS con los que se sincronizara este BBS: "
#ALLOWED_NODES = "Nodes with Access to this BBS: "
ALLOWED_NODES = "Nodos con Acceso a este BBS: "
#URGENT_ALLOWED_NODES = "Nodes with Urgent board permissions: "
URGENT_ALLOWED_NODES = "Nodos con permiso para publicar Anuncios Urgentes: "


###########
# LOGGING #
###########
RUNNING = "QXT-BBS se esta ejecutando en la interfaz: "
SHUTTING = "Apagando el QXT-BBS ..."


########
# MENU #
########
BBS_NAME = ".:: QXT BBS ::.\n"
#MAILS = "📰"
MAILS = "Mails No leidos:"
#BULLETIN_MENU = "📰BBS Menu📰"
BBS_MENU = ":: Menu BBS ::\n"
#Q ="Q"
Q = "C"
#QUICK_COMMANDS= "[Q]uick Commands"
QUICK_COMMANDS= "[C]omandos"
B = "B"
#BULLETIN = "[B]ulletins"
BULLETIN ="[B]oletines"
BBS = "[B]BS"
U = "U"
#UTILITIES = "[U]tilities"
UTILITIES = "[U]tilidades"
#X = "X"
X = "S"
#EXIT = "E[X]IT"
EXIT = "[S]alir"
M = "M"
MAIL= "[M]ail"
C = "E"
#MENU_CHANNEL_DIR = "[C]hannel Dir"
MENU_CHANNEL_DIR = "[E]nlaces"
J = "J"
JS8CALL = "[J]S8Call"
#S = "S"
S = "D"
#STATS = "[S]tats"
STATS = "[D]atos"
F = "F"
#FORTUNE = "[F]ortune"
FORTUNE = "[F]rases"
W = "W"
WALL = "[W]all of Shame"
#UTILITIES_MENU = "🛠️Utilities Menu🛠️"
UTILITIES_MENU = ":: Menu Utilidades ::\n"
#MAIL_MENU = "✉️Mail Menu✉️\nWhat would you like to do with mail?\n[R]ead  [S]end E[X]IT"
MAIL_MENU = ":: Menu Mail ::\nQue te gustaria hacer?\n[R]ead\n  [S]end\n  E[X]it"
#BULLETIN_MENU = "📰Bulletin Menu📰\nWhich board would you like to enter?\n[G]eneral  [I]nfo  [N]ews  [U]rgent"
BULLETIN_MENU = ":: Menu Boletines ::\nA que Boletin quieres entrar?\n[G]eneral\n  [I]nfo\n  [N]oticias\n  [U]rgente"
#STATS_MENU = "📊Stats Menu📊\nWhat stats would you like to view?\n[N]odes  [H]ardware  [R]oles  E[X]IT"
STATS_MENU = ":: Menu de Datos ::\n\nQue datos quieres ver?\n[N]odos\n  [H]ardware\n  [R]oles\n  ]S]alir"
#NO_FORTUNES = "No fortunes available."
NO_FORTUNES = "No hay frases celebres disponibles"
#TOTAL_NODES = "Total nodes seen: "
TOTAL_NODES = "Total de nodos: "
#HARDWARE_NODES = "Hardware Models: "
HARDWARE_NODES = "Modelos Hardware: "

########################
# MESSAGES PROCESING #
########################

#q = "q"
q = "c"
b = "b"
u = "u"
#x = "x"
x = "s"
m = "m"
c = "c"
j = "j"
#s = "s"
s = "d" 
f = "f"
w = "w"
n = "n"
h = "h" # Hardware
r = "r" # Role # Reply
e = "e"
p = "p"


################
# QUICK COMMANDS #
################

#QUICK_COMMANDS_MENU = "✈️QUICK COMMANDS✈️\nSend command below for usage info:\nSM,, - Send Mail\nCM - Check Mail\nPB,, - Post Bulletin\nCB,, - Check Bulletins\n"
QUICK_COMMANDS_MENU = "COMANDOS RAPIDOS\nTeclea algun comando para + info:\n[EM] Enviar Mail\n[CM] Chequear Mails\n[PB]  Publicar Boletin\n[CB] Chequear Boletines\n"
#sm = "sm,,"
sm = "em"
cm = "cm"
#pb = "pb,,"
pb = "pb"
#cb = "cb,,"
cb = "cb"
#FEEL_FREE = "Okay, feel free to send another command."
FEEL_FREE = "Ok, puedes enviar otro comando"

#############
# BULLETINS #
#############

GENERAL = "General"
INFO = "Info"
#NEWS = "News"
NEWS = "Noticias"
#URGENT = "Urgent"
URGENT = "Urgente"
#SUBJECT_BULLETIN = "What is the subject of your bulletin? Keep it short."
SUBJECT_BULLETIN = "Asunto de tu Boletin? Mantenlo corto."
#CONTENT_BULLETIN = "Send the contents of your bulletin. Send a message with END when finished."
CONTENT_BULLETIN = "Envia el texto de tu Boletin. Envia END para terminarlo."
#ERROR = "Error: Unable to retrieve your node information."
ERROR = "Error: imposible obtener informacion de tu nodo."
#YOUR_BULLETIN_1 = "Your bulletin "
#YOUR_BULLETIN_2 = "has been posted to "
YOUR_BULLETIN_1 = "Tu Boletin "
YOUR_BULLETIN_2 = " ha sido publicado en " 
#FORMAT_BULLETIN = "Post Bulletin Quick Command format:\nPB,,{board_name},,{subject},,{content}"
FORMAT_BULLETIN = "Formato de Comando para Publicar Boletin:\nPB,,{Nombre_Boletin},,{Asunto},,{Texto}"
#CHECK_BULLETIN = "Check Bulletins Quick Command format:\nCB,,{board_name}"
CHECK_BULLETIN = "Formato de Comando para Chequear Boletin:\nCB,,{Nombre_Boletib}"
#NO_BULLETIN = "No bulletins available on board: "
NO_BULLETIN = "No hay boletines disponibles en: "
#BULLETIN_NUM = "\nPlease reply with the number of the bulletin you want to read."
BULLETIN_NUM = "\nPor favor, responde con el numero del Boletin que quieres leer."
#INVALID_BULLETIN = "Invalid bulletin number. Please try again."
INVALID_BULLETIN = "Numero de Boletin invalido. Intentalo otra vez."

########
# MAIL #
########

#YOUR_MAIL_1 = "You have " 
YOUR_MAIL_1 = "Tienes " 
#YOUR_MAIL_2 = "mail messages. Select a message number to read:"
YOUR_MAIL_2 = "mail/s. Selecciona un numero para leer el mail:"
#DATE = "Date: "
DATE = "Fecha: "
#FROM = "From: "
FROM = "De: "
#SUBJECT = "Subject: " 
SUBJECT = "Asunto: " 
#NO_MAIL = "There are no messages in your mailbox.📭"
NO_MAIL = "No tienes mensajes."
#MAIL_TO = "What is the Short Name of the node you want to leave a message for?"
MAIL_TO = "Cual es el nombre corto del nodo al que quieres dejar un mensaje?"
#DO_MAIL = "What would you like to do with this message?\n[K]eep  [D]elete  [R]eply"
DO_MAIL = "Que quieres hacer con el mensaje?\n[K]Guardar\n  [D]Borrar\n  [R]esponder"
#NO_NODE = "I'm unable to find that node in my database."
NO_NODE = "Ese Nodo no existe en la Base de Datos."
#MAIL_SUBJECT = "What is the subject of your message to "
MAIL_SUBJECT = "Cual es el asunto de tu mensaje para "
#KEEP_SHORT = "Keep it short."
KEEP_SHORT = "Mantenlo corto"
#MULTIPLE_NODES = "There are multiple nodes with that short name. Which one would you like to leave a message for?"
MULTIPLE_NODES = "Hay varios nodos con ese Nombre Corto. A cual de ellos le quieres enviar el mensaje?"
#MSG_DELETED = "The message has been deleted 🗑️"
MSG_DELETED = "El mensaje ha sido borrado."
#FORMAT_MAIL = "Send Mail Quick Command format:\nSM,,{short_name},,{subject},,{message}"
FORMAT_MAIL = "Formato de Comando para enviar Mail:\nEM,,{Nombre_Corto},,{Asunto},,{Mensaje}"
#MSG_KEPT = "The message has been kept in your inbox.✉️"
MSG_KEPT = "El Mensaje ha sido guardo en un bandeja."
#MSG_REPLY_1 = "Send your reply to "
MSG_REPLY_1 = "Envia tus respuesta a "
#MSG_REPLY_2 = "now, followed by a message with END"
MSG_REPLY_2 = "termina tu mensaje con END"
#INVALID_MSG = "Invalid message number. Please try again."
INVALID_MSG = "Numero de Mensaje Invalido. Intenta otra vez."
#LONG_MSG = "Send your message. You can send it in multiple messages if it's too long for one.\nSend a single message with END when you're done"
LONG_MSG = "Envia tu Mail. Puedes enviar multiples mensajes si es muy largo para solo un mensaje. Envia END en un mensaje separado para terminar"
#FOLLOWING_MSG = "📬 You have the following messages:\n"
FOLLOWING_MSG = " Tienes los siguientes mensajes:\n"
#MSG_NUM = "\nPlease reply with the number of the message you want to read."
MSG_NUM = "\nPor favor, responde con el numero del mensaje que quieres leer."
#NEW_MAIL_1 = "You have a new mail message from "
NEW_MAIL_1 = "Tienes un nuevo Mail de "
#NEW_MAIL_2 = ". Check your mailbox by responding to this message with CM."
NEW_MAIL_2 = ". Chequear tu buzon de mail respondiendo a este mensaje con CM."
#MAIL_SENT = "Mail has been sent to "
MAIL_SENT = "Mail enviado a "
#NODE_NOT_FOUND = "Node short name not found: "
NODE_NOT_FOUND = "Nombre corto NO encontrado: "
#MAIL_POSTED = "Mail has been posted to the mailbox of "
MAIL_POSTED = "El Mail ha sido enviado en el buzon de "


# CHANNEL DIRECTORY #

#CHANNEL_DIR = "📚CHANNEL DIRECTORY📚\nWhat would you like to do?\n[V]iew  [P]ost  E[X]IT"
CHANNEL_DIR = "DIRECTORIO DE CANALES\nQue quieres hacer?\n[V]er\n  [P]ublicar\n  [X]Salir"
#CHANNEL_NUM = "Select a channel number to view:\n"
CHANNEL_NUM = "Selecciona el numero del canal para verlo"
#NO_CHANNELS = "No channels available in the directory."
NO_CHANNELS = "No hay Canales en el Directorio"
#CHANNEL_NAMED = "Name your channel for the directory:"
CHANNEL_NAMED = "Escribe el nombre para el Canal"
#CHANNEL_NAME = "Channel Name:"
CHANNEL_NAME = "Nombre del Canal"
#CHANNEL_URL = "Channel URL:"
CHANNEL_URL = "URL del Canal:"
#CHANNEL_PSK = "Send a message with your channel URL or PSK:"
CHANNEL_PSK = "Envia un mensaje con la URL o PSK del canal"
#CHANNEL_ADDED = " channel has been added to the directory."
CHANNEL_ADDED = " Canal agregado al directorio."
#FORMAT_CHANNEL = "Post Channel Quick Command format:\nCHP,,{channel_name},,{channel_url}"
FORMAT_CHANNEL = "Formato de Comando para Publicar Canal:\nCHP,,{channel_name},,{channel_url}"
#CHANNEL = "Channel "
CHANNEL = "Canal "
#AVAILABLE_CHANNELS = "Available Channels:\n"
AVAILABLE_CHANNELS = "Canales Disponibles:\n"
#CHANNEL_NUM_REPLY = "\nPlease reply with the number of the channel you want to view."
CHANNEL_NUM_REPLY = "\nPor favor, responde con el numero del Canal que quieres leer."
#INVALID_CHANNEL = "Invalid channel number. Please try again."
INVALID_CHANNEL = "Numero de Canal invalido. Intentalo de nuevo."


#################
# WALL OF SHAME #
#################

#LOW_BATT = "Devices with battery levels below 20%:\n"
LOW_BATT = "Nodos con nivel de bateria inferior al 20%:\n"
#NO_LOW = "No devices with battery levels below 20% found."
NO_LOW = "No hay Nodos con nivel de bateria inferior al 20%"