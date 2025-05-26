CREATE TABLE raw_categories (
    id TEXT,
    nom TEXT
);

CREATE TABLE raw_produits (
    id TEXT,
    nom TEXT,
    prix TEXT,
    categorie_id TEXT
);

CREATE TABLE raw_clients (
    id TEXT,
    nom TEXT,
    email TEXT,
    adresse TEXT
);

CREATE TABLE raw_ventes (
    id TEXT,
    client_id TEXT,
    produit_id TEXT,
    quantite TEXT,
    date_vente TEXT
);

CREATE TABLE raw_paiements (
    id TEXT,
    vente_id TEXT,
    montant TEXT,
    mode_paiement TEXT,
    date_paiement TEXT
);