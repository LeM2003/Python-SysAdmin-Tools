# 🛠️ Python SysAdmin Tools

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Security](https://img.shields.io/badge/Security-Tools-red?style=for-the-badge)

**Collection d'outils d'administration système et cybersécurité**

</div>

---

## 📋 À propos

Ce dépôt regroupe mes **scripts Python** développés dans le cadre de mon auto-formation en **Administration Système** et **Cybersécurité**. Ces outils démontrent mes compétences en automatisation, sécurité réseau et scripting système.

---

## 📂 Contenu du Dépôt

### 1. 🔍 `scanner.py` - Scanner de Ports TCP

Un script d'analyse réseau utilisant la bibliothèque `socket` pour identifier les ports ouverts sur une machine cible.

**Objectif** : Identifier les services vulnérables ou accessibles sur un réseau pour audits de sécurité.

**Fonctionnalités** :
- ✅ Résolution DNS automatique
- ✅ Scan de plages de ports personnalisables
- ✅ Gestion des erreurs (Timeout, connexion refusée)
- ✅ Affichage des résultats en temps réel
- ✅ Identification des services courants (HTTP, SSH, FTP, etc.)

**Technologies** : Python 3, socket library

---

## 🚀 Installation & Utilisation

### Prérequis

- Python 3.8 ou supérieur
- Système Linux/Unix (recommandé) ou Windows
- Permissions réseau appropriées

### Installation

```bash
# Cloner le dépôt
git clone https://github.com/LeM2003/Python-SysAdmin-Tools.git
cd Python-SysAdmin-Tools

# (Optionnel) Créer un environnement virtuel
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Installer les dépendances (si nécessaire)
pip install -r requirements.txt
```

### Utilisation du Scanner de Ports

```bash
# Scanner les ports courants (1-1024)
python scanner.py <adresse_ip>

# Scanner une plage spécifique
python scanner.py <adresse_ip> <port_debut> <port_fin>

# Exemple
python scanner.py 192.168.1.1 1 100
```

**Exemple de sortie** :
```
[*] Résolution de l'hôte : 192.168.1.1
[*] Scan en cours...
[+] Port 22 ouvert - SSH
[+] Port 80 ouvert - HTTP
[+] Port 443 ouvert - HTTPS
[*] Scan terminé. 3 ports ouverts trouvés.
```

---

## ⚠️ Avertissement Légal

**IMPORTANT** : Ces outils sont destinés à des fins **éducatives** et d'**audit de sécurité autorisé** uniquement.

- ❌ **N'utilisez JAMAIS ces scripts sur des systèmes sans autorisation explicite**
- ✅ Utilisez-les uniquement sur vos propres systèmes ou avec permission écrite
- ⚖️ L'utilisation non autorisée peut constituer une **violation de la loi**

L'auteur décline toute responsabilité en cas d'utilisation abusive.

---

## 🎯 Compétences Démontrées

Ce projet met en avant ma maîtrise de :

- **Python** - Scripting avancé et programmation réseau
- **Sécurité Réseau** - Analyse de ports, détection de services
- **Administration Système** - Automatisation, gestion de logs
- **Bonnes Pratiques** - Gestion d'erreurs, code documenté
- **Linux** - Environnement Unix/Linux

---

## 🗺️ Roadmap

Outils à venir :

- [ ] **Analyseur de logs** - Parser et analyser les logs système (auth.log, syslog)
- [ ] **Moniteur de processus** - Surveillance CPU/RAM avec alertes
- [ ] **Gestionnaire de backup** - Automatisation de sauvegardes
- [ ] **Détecteur d'intrusion** - Analyse de trafic réseau anormal
- [ ] **Script de hardening** - Renforcement de sécurité système

---

## 📚 Ressources & Apprentissage

Ces scripts ont été développés en s'appuyant sur :

- 📖 Documentation officielle Python
- 🔒 OWASP Testing Guide
- 🌐 Cours d'administration système Linux
- 💻 Pratique sur environnements de test (VM, labs)

---

## 🤝 Contribution

Les contributions, suggestions et améliorations sont les bienvenues !

1. **Fork** le projet
2. Créer une branche (`git checkout -b feature/AmeliorationScanner`)
3. Commit les changements (`git commit -m 'Amélioration du scanner'`)
4. Push vers la branche (`git push origin feature/AmeliorationScanner`)
5. Ouvrir une **Pull Request**

---

## 📄 Licence

Ce projet est sous licence **MIT** - voir le fichier [LICENSE](LICENSE) pour plus de détails.

```
Copyright (c) 2024 Mouhamadou Diouf
```

---

## 👨‍💻 Auteur

<div align="center">

### **Mouhamadou Diouf**

🎓 Étudiant en **Master Data Science & Intelligence Artificielle**  
📍 Swiss UMEF University - Dakar, Sénégal

🎓 **Licence Statistique et Informatique Décisionnelle**  
📍 BEM Dakar | Diplômé le 31 août 2025

---

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Mouhamadou_Diouf-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mouhamadou-diouf-364309276)
[![GitHub](https://img.shields.io/badge/GitHub-@LeM2003-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/LeM2003)
[![Email](https://img.shields.io/badge/Email-dioufmouha71@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:dioufmouha71@gmail.com)

**Compétences** : Python • R • SQL • PHP • Linux • Cybersecurity • Data Analysis

---

**Made with ❤️ in Dakar, Senegal 🇸🇳**

</div>

---

## 🔗 Mes Autres Projets

- 💰 [**EcoTrack**](https://github.com/LeM2003/ecotrack) - Application de gestion financière (Projet de mémoire)
- 🎓 [**EduPlan**](https://github.com/LeM2003/eduplan) - Dashboard éducatif multi-utilisateur
- 📦 [**ImportManager-SN**](https://github.com/LeM2003/importmanager-sn) - Système de gestion d'importation

---

<div align="center">

[![Stars](https://img.shields.io/github/stars/LeM2003/Python-SysAdmin-Tools?style=social)](https://github.com/LeM2003/Python-SysAdmin-Tools)
[![Forks](https://img.shields.io/github/forks/LeM2003/Python-SysAdmin-Tools?style=social)](https://github.com/LeM2003/Python-SysAdmin-Tools/fork)

*Si ce projet vous aide, n'hésitez pas à lui donner une ⭐ !*

</div>
