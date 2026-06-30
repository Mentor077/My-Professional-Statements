"""
⚙️ FICHIER DE CONFIGURATION CENTRALE - PORTFOLIO DATA ANALYST
💼 Développeur : Mentor Malonga (Data Analyst @ Tecno)
🎯 Rôle : Centraliser les chemins de fichiers, les paramètres de KPIs et la connexion SQL.
"""

import os

# ==============================================================================
# 1. CONFIGURATION DES CHEMINS DE DONNÉES (Gestion Inventaire & Ventes)
# ==============================================================================
# Définit automatiquement le dossier racine du projet pour éviter les erreurs de chemin
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATHS = {
    "sales_raw": os.path.join(BASE_DIR, "data", "raw", "ventes_tecno_brutes.xlsx"),
    "inventory_raw": os.path.join(BASE_DIR, "data", "raw", "inventaire_stock.xlsx"),
    "cleaned_data": os.path.join(BASE_DIR, "data", "processed", "data_analyse_propre.csv"),
    "export_reports": os.path.join(BASE_DIR, "reports", "tableaux_de_bord/")
}

# ==============================================================================
# 2. SEUILS ET PARAMÈTRES DES KPIs (Pour les alertes de stock et ventes)
# ==============================================================================
KPI_THRESHOLDS = {
    "SEUIL_ALERTE_STOCK_MIN": 15,       # Alerte si un modèle Tecno a moins de 15 unités
    "OBJECTIF_VENTES_MENSUEL": 500,     # Objectif de vente global en unités
    "MARGE_BENEFICIAIRE_CIBLE": 0.12,   # Objectif de marge minimum (12%)
}

# ==============================================================================
# 3. BENCHMARKING & PARAMÈTRES MARCHÉ (Analyse comparative)
# ==============================================================================
BENCHMARK_CONFIG = {
    "MARQUES_CONCURRENTES": ["Samsung", "Infinix", "Xiaomi", "Itel"],
    "ANNEE_REFERENCE": 2026,
    "ZONE_GEOGRAPHIQUE": "Brazzaville, Congo"
}

# ==============================================================================
# 4. CONFIGURATION SÉCURISÉE DE LA BASE DE DONNÉES (SQL)
# ==============================================================================
# Utilisation de variables d'environnement pour ne pas afficher vos mots de passe sur GitHub
DB_CONFIG = {
    "HOST": os.getenv("TECNO_DB_HOST", "localhost"),
    "PORT": os.getenv("TECNO_DB_PORT", "5432"),
    "NAME": os.getenv("TECNO_DB_NAME", "tecno_sales_db"),
    "USER": os.getenv("TECNO_DB_USER", "postgres"),
    "PASS": os.getenv("TECNO_DB_PASS", "VotreMotDePasseSecurise")
}

def get_sql_connection_string():
    """Génère la chaîne de connexion pour SQLAlchemy (Pandas/Python)"""
    return f"postgresql://{DB_CONFIG['USER']}:{DB_CONFIG['PASS']}@{DB_CONFIG['HOST']}:{DB_CONFIG['PORT']}/{DB_CONFIG['NAME']}"

# ==============================================================================
# 5. CONFIGURATION DE L'AFFICHAGE DES GRAPHIQUES (Seaborn / Matplotlib)
# ==============================================================================
GRAPH_STYLE = {
    "THEME": "whitegrid",
    "PALETTE_COULEURS": "Blues_d",  # Palette bleutée pour correspondre à l'identité Tecno
    "TAILLE_FIGURE": (12, 6)
}
