-- =============================================================
-- Archivo: banco.sql
-- Autor: Ever Nuñez
-- Descripción: Script para crear una base de datos de simulador bancario
-- Motor: Microsoft SQL Server
-- Fecha: 2025-10-14
-- =============================================================

-- 1️⃣ CREAR BASE DE DATOS
CREATE DATABASE BancoPython;
GO

-- Usar la base de datos
USE BancoPython;
GO

-- 2️⃣ TABLA CLIENTES
CREATE TABLE Clientes (
    id_cliente INT IDENTITY(1,1) PRIMARY KEY,
    nombre NVARCHAR(100) NOT NULL,
    dni CHAR(8) UNIQUE NOT NULL,
    telefono NVARCHAR(15),
    direccion NVARCHAR(150),
    fecha_registro DATETIME DEFAULT GETDATE()
);
GO

-- 3️⃣ TABLA CUENTAS
CREATE TABLE Cuentas (
    id_cuenta INT IDENTITY(1,1) PRIMARY KEY,
    id_cliente INT NOT NULL,
    tipo NVARCHAR(50) CHECK (tipo IN ('Ahorros', 'Corriente')),
    saldo DECIMAL(12,2) DEFAULT 0,
    fecha_apertura DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente)
);
GO

-- 4️⃣ TABLA TRANSACCIONES
CREATE TABLE Transacciones (
    id_transaccion INT IDENTITY(1,1) PRIMARY KEY,
    id_cuenta INT NOT NULL,
    tipo NVARCHAR(50) CHECK (tipo IN ('Depósito', 'Retiro', 'Transferencia', 'Préstamo', 'Inversión')),
    monto DECIMAL(12,2) NOT NULL,
    descripcion NVARCHAR(200),
    fecha DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (id_cuenta) REFERENCES Cuentas(id_cuenta)
);
GO

-- 5️⃣ TABLA PRÉSTAMOS
CREATE TABLE Prestamos (
    id_prestamo INT IDENTITY(1,1) PRIMARY KEY,
    id_cliente INT NOT NULL,
    monto DECIMAL(12,2) NOT NULL,
    interes DECIMAL(5,2) DEFAULT 10.00,
    total_pagar AS (monto + (monto * interes / 100.0)) PERSISTED,
    estado NVARCHAR(20) DEFAULT 'Activo',
    fecha_solicitud DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente)
);
GO

-- 6️⃣ TABLA INVERSIONES
CREATE TABLE Inversiones (
    id_inversion INT IDENTITY(1,1) PRIMARY KEY,
    id_cliente INT NOT NULL,
    monto DECIMAL(12,2) NOT NULL,
    tasa DECIMAL(5,2) DEFAULT 5.00,
    ganancia AS (monto * tasa / 100.0) PERSISTED,
    fecha_inicio DATETIME DEFAULT GETDATE(),
    fecha_fin DATETIME NULL,
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente)
);
GO

-- 7️⃣ INSERTAR DATOS DE EJEMPLO
INSERT INTO Clientes (nombre, dni, telefono, direccion)
VALUES 
('Juan Pérez', '12345678', '987654321', 'Av. Siempre Viva 123'),
('María López', '87654321', '912345678', 'Jr. Los Olivos 45'),
('Ever Nuñez', '56781234', '900123456', 'Av. Central 321');
GO

INSERT INTO Cuentas (id_cliente, tipo, saldo)
VALUES 
(1, 'Ahorros', 1500.00),
(2, 'Corriente', 2500.00),
(3, 'Ahorros', 5000.00);
GO

INSERT INTO Transacciones (id_cuenta, tipo, monto, descripcion)
VALUES 
(1, 'Depósito', 500.00, 'Depósito inicial'),
(2, 'Retiro', 200.00, 'Pago de servicios'),
(3, 'Inversión', 1000.00, 'Inversión a corto plazo');
GO

INSERT INTO Prestamos (id_cliente, monto, interes)
VALUES 
(1, 1000.00, 8.5),
(3, 2000.00, 10.0);
GO

INSERT INTO Inversiones (id_cliente, monto, tasa)
VALUES 
(2, 1500.00, 6.0),
(3, 3000.00, 5.5);
GO

-- 8️⃣ CONSULTAS DE PRUEBA
-- Mostrar todos los clientes y sus cuentas
SELECT c.nombre, cu.tipo, cu.saldo
FROM Clientes c
JOIN Cuentas cu ON c.id_cliente = cu.id_cliente;

-- Mostrar todas las transacciones
SELECT t.id_transaccion, c.nombre AS Titular, t.tipo, t.monto, t.descripcion, t.fecha
FROM Transacciones t
JOIN Cuentas cu ON t.id_cuenta = cu.id_cuenta
JOIN Clientes c ON cu.id_cliente = c.id_cliente;

-- Mostrar préstamos activos
SELECT c.nombre, p.monto, p.interes, p.total_pagar, p.estado
FROM Prestamos p
JOIN Clientes c ON p.id_cliente = c.id_cliente
WHERE p.estado = 'Activo';

-- Mostrar inversiones y ganancias
SELECT c.nombre, i.monto, i.tasa, i.ganancia
FROM Inversiones i
JOIN Clientes c ON i.id_cliente = c.id_cliente;
GO
