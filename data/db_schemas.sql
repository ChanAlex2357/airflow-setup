-- Table des catégories
CREATE TABLE categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL
);

-- Table des produits
CREATE TABLE produits (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    prix DECIMAL(10,2) NOT NULL,
    categorie_id INT,
    FOREIGN KEY (categorie_id) REFERENCES categories(id)
);

-- Table des clients
CREATE TABLE clients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    adresse VARCHAR(255)
);

-- Table des ventes
CREATE TABLE ventes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT,
    produit_id INT,
    quantite INT,
    date_vente DATE,
    FOREIGN KEY (client_id) REFERENCES clients(id),
    FOREIGN KEY (produit_id) REFERENCES produits(id)
);

-- Table des paiements
CREATE TABLE paiements (
    id INT AUTO_INCREMENT PRIMARY KEY,
    vente_id INT,
    montant DECIMAL(10,2),
    mode_paiement VARCHAR(50),
    date_paiement DATE,
    FOREIGN KEY (vente_id) REFERENCES ventes(id)
);
