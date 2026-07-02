---
layout: default
title: MAP Transport Performance Dashboard
---

<table border="0" cellpadding="0" cellspacing="0">
  <tr>
    <!-- Colonne Gauche : Ton image locale chargée automatiquement -->
    <td valign="middle" width="70">
      <img src="image_projet1.jpg" alt="Logo Projet" width="55" height="55" style="border-radius: 8px;">
    </td>
    <!-- Colonne Droite : Ton Titre parfaitement aligné horizontalement -->
    <td valign="middle">
      <h1>MAP Transport Performance Dashboard</h1>
    </td>
  </tr>
</table>

> 🚢 Tableau de bord décisionnel — Analyse de performance commerciale et logistique (2021-2024)

⬅️ [**Retour au Profil Principal**](README.md)

---

## 1️⃣ Introduction du Projet

**MAP Transport** est une entreprise de transport multimodal (maritime, routier, aérien, fluvial).  

Dans un contexte de forte concurrence, la direction avait besoin d'un outil unique pour **piloter sa performance commerciale**, suivre ses revenus et comprendre pourquoi certains prospects ne se transformaient pas en clients.

J'ai conçu un **tableau de bord interactif Power BI** structuré en **2 vues analytiques majeures** couvrant **4 années d'activité (2021-2024)**, transformant des milliers de lignes de données brutes en un outil de décision clair et visuel.

🎯 **Objectif :** Offrir une vision à 360° du cycle commercial — du prospect jusqu'au client confirmé.

---

## 🎨 Les 2 Vues Déployées (Aperçu du Rapport Power BI)

### 📊 Vue 1 — Le Dashboard Général
<p align="center">
  <img src="map-first.jpg" width="900" alt="Dashboard Général - MAP Transport">
</p>

> Cette première vue offre un pilotage macro-économique global. Elle met en évidence la trajectoire des revenus annuels, la performance brute par type de prestation (Air, Sea, Road, River) ainsi que la concentration des parts de marché du Top 3 des compagnies clientes.

---

### 📈 Vue 2 — Le Tableau de Détail des Indicateurs
<p align="center">
  <img src="map-second.jpg" width="900" alt="Tableau de Détail des Indicateurs - MAP Transport">
</p>

> Cette seconde vue est orientée sur le diagnostic des volumes financiers. Elle segmente de manière croisée les montants prospectés, confirmés, perdus et en attente afin d'identifier avec précision quelles structures ou destinations génèrent les plus fortes pertes commerciales.

---

## 2️⃣ Détail du Travail Réalisé

Le projet s'est déroulé en plusieurs phases clés :

### 🔹 Collecte & Préparation des données (ETL)
- Importation des bases de données de facturation, prospects et clients.
- Nettoyage rigoureux sous Power Query (traitement des valeurs manquantes, doublons et reclassification des entrées "Unknown").
- Structuration par année, prestation, destination et entreprise.

### 🔹 Modélisation Relationnelle
- Création du modèle de données en étoile.
- Établissement des relations de type 1-à-plusieurs entre les tables de dimensions (Prestations, Temps, Clients) et la table de faits.

### 🔹 Conception des Indicateurs Métier (DAX)
- Modélisation de **8 KPIs stratégiques** en langage DAX (Factures envoyées, confirmées, revenus totaux, opportunités en attente et manques à gagner).
- Formulation du **taux de conversion global** prospect ➔ client.

---

## 3️⃣ Outils Utilisés

| Outil | Utilisation |
|-------|-------------|
| **Power BI Desktop** | Développement de l'interface et des visualisations interactives |
| **Power Query** | Processus d'Extraction, Transformation et Chargement (ETL) |
| **Langage DAX** | Écriture des mesures calculées, cumuls annuels et analyses de parts de marché |
| **Data Modeling** | Architecture relationnelle de la base de données décisionnelle |

---

## 4️⃣ Analyse & Insights Stratégiques

L'exploration visuelle de la donnée a révélé des opportunités et des points d'attention majeurs :

### 📈 Performance Globale
- 💰 **Revenu total confirmé :** 1.22 Md FCFA.
- 📨 **637 factures émises** pour **263 confirmées**, soit un taux de conversion d'environ **41 %**.
- 🏆 **86 clients gagnés** sur un portefeuille de 120 compagnies prospectées.

### ⚠️ Diagnostic des Pertes Commerciales
- 💸 **Montant perdu (1.93 Md FCFA) :** Supérieur aux gains confirmés, révélant une fuite importante lors du tunnel de conversion.
- 📉 **Alerte 2023 :** Année critique enregistrant le pic historique de pertes (676 M FCFA).
- ⏳ **En attente (390.92 M FCFA) :** Représente un gisement de valeur à relancer d'urgence.

---

## 5️⃣ Solutions & Recommandations

| Problème identifié | Solution propsée |
|--------------------|-------------------|
| 💸 Pertes commerciales élevées | Mettre en place un audit systématique des motifs de refus sur les devis perdus |
| ⏳ 390 M FCFA en attente | Automatiser les alertes de relance sur WhatsApp/Email pour les dossiers suspendus |
| 🚢 SEA : Forte prospection, faible marge | Réévaluer la grille tarifaire ou optimiser les coûts opérationnels du fret maritime |
| ✈️ AIR : Rentabilité maximale (580 M FCFA) | Réallouer le budget marketing pour capturer plus de parts sur le segment aérien |

---

<p align="center">
  ⬅️ <a href="README.md"><b>[Retour au Profil Principal]</b></a>
</p>
