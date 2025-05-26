-- Insertion des catégories
INSERT INTO categories (nom) VALUES
('Électronique'),
('Vêtements'),
('Alimentation');

-- Insertion des produits
INSERT INTO produits (nom, prix, categorie_id) VALUES
('Smartphone', 299.99, 1),
('T-shirt', 19.99, 2),
('Pain', 2.49, 3),
('Ordinateur portable', 799.99, 1),
('Jeans', 49.99, 2);

-- Insertion des clients
INSERT INTO clients (nom, email, adresse) VALUES
('Alice Dupont', 'alice@example.com', '123 Rue Principale'),
('Bob Martin', 'bob@example.com', '456 Avenue des Champs'),
('Charlie Durand', 'charlie@example.com', '789 Boulevard Central'),
('Diane Petit', 'diane@example.com', '321 Route de la Gare'),
('Éric Moreau', 'eric@example.com', '654 Chemin du Lac');

-- Insertion des ventes
INSERT INTO ventes (client_id, produit_id, quantite, date_vente) VALUES
(1, 1, 1, '2025-05-01'),
(2, 2, 2, '2025-05-02'),
(3, 3, 5, '2025-05-03'),
(4, 4, 1, '2025-05-04'),
(5, 5, 1, '2025-05-05'),
(1, 2, 3, '2025-05-06'),
(2, 3, 2, '2025-05-07'),
(3, 1, 1, '2025-05-08'),
(4, 5, 2, '2025-05-09'),
(5, 4, 1, '2025-05-10');

-- Insertion des paiements pour 5 ventes
INSERT INTO paiements (vente_id, montant, mode_paiement, date_paiement) VALUES
(1, 299.99, 'Carte de crédit', '2025-05-01'),
(2, 39.98, 'PayPal', '2025-05-02'),
(3, 12.45, 'Espèces', '2025-05-03'),
(4, 799.99, 'Carte de crédit', '2025-05-04'),
(5, 49.99, 'Virement bancaire', '2025-05-05');
