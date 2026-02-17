<?php
include "dbConnection.php";
Header('Content-Type: application/json');

// Verifica si faltan datos requeridos
if (!isset($_POST['userName'], $_POST['email'], $_POST['pass'])) {
    echo json_encode(['done' => false, 'message' => 'Faltan datos requeridos']);
    exit();
}

$userName = $_POST['userName'];
$email = $_POST['email'];
$pass = hash("sha256", $_POST['pass']); // Hash de la contraseña

try {
    // Verificar si el nombre de usuario ya existe
    $sql = "SELECT userName FROM usuarios WHERE userName = :userName";
    $stmt = $pdo->prepare($sql);
    $stmt->bindParam(':userName', $userName);
    $stmt->execute();
    
    if ($stmt->rowCount() > 0) {
        echo json_encode(['done' => false, 'message' => 'Error: nombre de usuario ya existe']);
        exit();
    }

    // Verificar si el correo ya existe
    $sql = "SELECT email FROM usuarios WHERE email = :email";
    $stmt = $pdo->prepare($sql);
    $stmt->bindParam(':email', $email);
    $stmt->execute();

    if ($stmt->rowCount() > 0) {
        echo json_encode(['done' => false, 'message' => 'Error: email ya existe']);
        exit();
    }

    // Insertar el nuevo usuario en la base de datos
    $sql = "INSERT INTO usuarios (userName, email, password) VALUES (:userName, :email, :password)";
    $stmt = $pdo->prepare($sql);
    $stmt->bindParam(':userName', $userName);
    $stmt->bindParam(':email', $email);
    $stmt->bindParam(':password', $pass);

    // Si se ejecuta correctamente, devolver éxito
    if ($stmt->execute()) {
        echo json_encode(['done' => true, 'message' => 'Felicitaciones, usuario creado correctamente']);
    } else {
        echo json_encode(['done' => false, 'message' => 'Error al crear el usuario']);
    }
} catch (PDOException $e) {
    // Devolver mensaje de error en caso de excepción
    echo json_encode(['done' => false, 'message' => 'Error de base de datos: ' . $e->getMessage()]);
}
exit();
?>