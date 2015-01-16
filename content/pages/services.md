Title: Services

Notre structure met à votre disposition dès l'ouverture les services suivants :

* **VLAN de Peering Public** : C'est le cœur du GIX, un VLAN dans lequel circulera le trafic entre membres IPv4 et IPv6. Seul le peering public est autorisé sur ce VLAN via les serveurs de routes. Tout autre usage est prescrit de ce VLAN.
* **Serveurs de routes** : Ce service va de pair avec le VLAN de Peering Public et vous permettra de n'avoir à monter qu'une session BGP avec les Serveurs de Routes. Ceci permettra ainsi d'échanger de façon simple et efficace avec les autres utilisateurs du GIX sans devoir monter une session par ASN. Chaque nouveau utilisateur sera donc dès sa connexion immédiatement propagé à vos routeurs sans plus d'effort de votre part.
* **Serveur NTP** : Ce serveur vous permettra d'avoir localement une référence pour synchroniser vos horloges via le protocole NTP.
* **VLAN Privé** : Ce service permet la mise en place de différents services entre deux membres ou plus. Il permet entre autre de fournir du Peering Privé, du Transit IP, des services de VOIP, etc. 

À venir dans un futur proche

* **Interconnexion GIX2GIX** : Nous mettrons en place ultérieurement des interconnexions avec les IX régionaux proches ainsi que nationaux tel TOUIX, LYONIX et FRANCEIX sur les services de Peering Public. Ce service sera limité en débit par utilisateur/destination afin de ne pas concurrencer les GIX entre eux ainsi que les fournisseurs de bande passante L2, tout en permettant aux petits acteurs d'accéder aux facilités du peering avec les utilisateurs d'autres régions.
* **Un Portail Public** : Ce site regroupera les statistiques publique du GIX ainsi que l'état du réseau.
* **Un Portail Extranet** : Cet espace utilisateur unique regroupera toutes les informations liés aux statistiques, aux tickets d'incidents, aux commandes de ports... 


