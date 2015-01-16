Title: Mieux comprendre les GIX
Date: 2015-01-16

## Au début, était l'Internet !

L'Internet est ce que l'on appelle le "réseau des réseaux". Mais pour commencer qu'est-ce donc un réseau ?

Un réseau est un ensemble d'équipements informatiques qui sont reliés ensemble. Pour relier ces équipements, on utilise dans la majorité des cas un switch ou commutateur réseau qui permet de renvoyer l'information au bon (à tous) PC relié(s).

Dans le cas de gros réseaux, on relie plusieurs switchs ensemble.


L'Internet est un ensemble de réseaux qui sont reliés entre eux.

Ces réseaux sont ceux des Fournisseurs d'Accès Internet (Orange, Free, SFR), des hébergeurs, des grands réseaux IP (Renater, Amplivia, réseaux de grandes entreprises, ...) ou des opérateurs Télécoms ayant aussi une activité IP (France Telecom, SFR-Neuf-Cegetel…). Ces réseaux sont référencés par un numéro appelé Autonomous System (AS).

Mais quand on envoie des informations - en fait, des paquets IP - à une machine qui se situe sur un autre AS, comment ça marche ? Il y a 2 possibilités : 

* Soit les 2 AS échangent leurs paquets IP sur un GIX, 
* Soit les 2 AS ne sont pas reliés l'un à l'autre directement. Le trafic passe alors par des opérateurs plus importants (transit provider) qui s'échangent entre eux le trafic (souvent sur des nœuds d'échange ou bien eux-même remontent encore d'un niveau jusqu'à trouver un noeud d'échange). 

L'ensemble du trafic Internet passe par des noeuds d'échanges Internet ou des GIX. On comprend donc l'intérêt d'un nœud d'échange qui va limiter le nombre d'intermédiaires pour transporter les informations d'une source à une destination. 

## Définitions

**Commutateur** : Équipement de réseau qui reçoit des signaux d'une ligne en entrée et les transfère vers une ligne en sortie. Il interconnecte ainsi deux segments d'un réseau. Le commutateur (en anglais Switch) assure soit de la commutation de circuits soit de la transmission de paquets. Différents types de commutateurs existent selon le niveau hiérarchique auquel ils sont placés dans un réseau. Un commutateur optimise l'utilisation de la bande passante dans la gestion du trafic. La programmation logique des commutateurs permet en effet de paramétrer et d'optimiser l'organisation du trafic sur le réseau. Le commutateur utilise les adresses dites MAC (Medium Access Control) qui sont les identifiants des équipements physiques du réseau pour acheminer le trafic. Un commutateur d'adonnés (CAA) analyse le signal et sélectionne la bonne sortie automatiquement. 

**Réseaux IP** : Les réseaux IP sont caractérisés par une indépendance par rapport au matériel et la possibilité d'établir une communication entre deux machines situées sur des réseaux différents. 

**IP** : Protocole de transfert d'information utilisé pour l'Internet. Il découpe l'information en paquets dits "datagrammes" qu'il route en passant d'un point à un autre du réseau jusqu'à destination grâce aux adresses de réseaux et sous réseaux qui lui sont données. Le protocole IP assure, outre le routage, la délivrance des datagrammes à leur destinataire, ceux-ci pouvant suivre des chemins différents sur le réseau. Ce transfert peut utiliser diverses technologies support : TCP, Ethernet, ATM. Le mode IP natif est celui dans lequel la couche 3 du modèle OSI est en IP, autrement dit le protocole IP n'est pas encapsulé dans un autre mode de transmission. Il est alors le plus souvent associé au protocole de transmission Ethernet. 

**Trafic Internet** : Le terme fait référence à la circulation des flux d'information sur le réseau informatique mondial Internet.
