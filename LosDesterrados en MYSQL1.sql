CREATE DATABASE LosDesterrados;

USE LosDesterrados;

CREATE TABLE Cultivos (
    id_cultivo INT PRIMARY KEY AUTO_INCREMENT,
    tipo_planta VARCHAR(100),
    fecha_siembra DATE,
    estado_crecimiento VARCHAR(50),
    rendimiento_esperado DECIMAL(10, 2)
);

CREATE TABLE Insumos (
    id_insumo INT PRIMARY KEY AUTO_INCREMENT,
    tipo_insumo VARCHAR(100),
    cantidad_disponible DECIMAL(10, 2),
    fecha_caducidad DATE
);

CREATE TABLE Clientes (
    id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100),
    correo VARCHAR(100),
    telefono VARCHAR(15)
);

CREATE TABLE Ventas (
    id_venta INT PRIMARY KEY AUTO_INCREMENT,
    cliente_id INT,
    fecha_venta DATETIME,
    total DECIMAL(10, 2),
    FOREIGN KEY (cliente_id) REFERENCES Clientes(id_cliente)
);

CREATE TABLE Detalle_Venta (
    id_detalle INT PRIMARY KEY AUTO_INCREMENT,
    venta_id INT,
    cultivo_id INT,
    cantidad DECIMAL(10, 2),
    subtotal DECIMAL(10, 2),
    FOREIGN KEY (venta_id) REFERENCES Ventas(id_venta),
    FOREIGN KEY (cultivo_id) REFERENCES Cultivos(id_cultivo)
);

CREATE TABLE Compras (
    id_compra INT PRIMARY KEY AUTO_INCREMENT,
    insumo_id INT,
    fecha_compra DATE,
    cantidad_comprada DECIMAL(10, 2),
    total_compra DECIMAL(10, 2),
    FOREIGN KEY (insumo_id) REFERENCES Insumos(id_insumo)
);

CREATE TABLE Detalle_Cultivo (
    id_detalle INT PRIMARY KEY AUTO_INCREMENT,
    cultivo_id INT,
    insumo_id INT,
    cantidad_usada DECIMAL(10, 2),
    FOREIGN KEY (cultivo_id) REFERENCES Cultivos(id_cultivo),
    FOREIGN KEY (insumo_id) REFERENCES Insumos(id_insumo)
);

-- Inserción de registros en la tabla Cultivos
INSERT INTO Cultivos (tipo_planta, fecha_siembra, estado_crecimiento, rendimiento_esperado) VALUES
('Tomate', '2024-01-15', 'Crecimiento', 1000.00),
('Lechuga', '2024-02-20', 'Cosechado', 500.00),
('Pepino', '2024-03-05', 'Crecimiento', 800.00);

-- Inserción de registros en la tabla Insumos
INSERT INTO Insumos (tipo_insumo, cantidad_disponible, fecha_caducidad) VALUES
('Fertilizante', 1500.00, '2025-06-01'),
('Semillas de tomate', 300.00, '2024-12-15'),
('Insecticida', 200.00, '2025-03-01');

-- Inserción de registros en la tabla Clientes
INSERT INTO Clientes (nombre, correo, telefono) VALUES
('Juan Pérez', 'juan.perez@example.com', '1234567890'),
('María López', 'maria.lopez@example.com', '0987654321'),
('Carlos Ruiz', 'carlos.ruiz@example.com', '5555555555');

-- Inserción de registros en la tabla Ventas
INSERT INTO Ventas (cliente_id, fecha_venta, total) VALUES
(1, '2024-10-05 10:00:00', 200.00),
(2, '2024-10-10 14:30:00', 150.00),
(3, '2024-10-15 09:15:00', 300.00);

-- Inserción de registros en la tabla Detalle_Venta
INSERT INTO Detalle_Venta (venta_id, cultivo_id, cantidad, subtotal) VALUES
(1, 1, 10, 100.00),
(1, 2, 5, 50.00),
(2, 1, 8, 80.00),
(2, 3, 5, 70.00),
(3, 2, 12, 120.00),
(3, 3, 10, 180.00);

-- Inserción de registros en la tabla Compras
INSERT INTO Compras (insumo_id, fecha_compra, cantidad_comprada, total_compra) VALUES
(1, '2024-10-01', 200.00, 1000.00),
(2, '2024-10-05', 150.00, 450.00),
(3, '2024-10-10', 100.00, 300.00);

-- Consulta para obtener las ventas por tipo de cultivo
SELECT c.tipo_planta AS tipo_planta, 
       SUM(dv.cantidad) AS total_vendido, 
       SUM(dv.subtotal) AS ingresos
FROM Detalle_Venta dv
JOIN Cultivos c ON dv.cultivo_id = c.id_cultivo
JOIN Ventas v ON dv.venta_id = v.id_venta
WHERE v.fecha_venta BETWEEN '2024-10-01' AND '2024-10-31'  -- Ajusta el rango de fechas
GROUP BY c.tipo_planta;

-- Consulta de las compras de insumos 
SELECT i.tipo_insumo AS tipo_insumo, 
       SUM(c.cantidad_comprada) AS total_comprado, 
       SUM(c.total_compra) AS total_gasto
FROM Compras c
JOIN Insumos i ON c.insumo_id = i.id_insumo
WHERE c.fecha_compra BETWEEN '2024-10-01' AND '2024-10-31'  -- Ajusta el rango de fechas
GROUP BY i.tipo_insumo;