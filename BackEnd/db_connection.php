<?php
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST');
header('Access-Control-Allow-Headers: Content-Type');

// Datenbankverbindungsdaten
$host = 'localhost';
$user = 'flaskuser';
$password = 'flaskpass';
$database = 'search_ai_maindb';

// Verbindung zur Datenbank herstellen
$conn = new mysqli($host, $user, $password, $database);

// Überprüfen der Verbindung
if ($conn->connect_error) {
    die(json_encode([
        'success' => false,
        'message' => 'Verbindungsfehler: ' . $conn->connect_error
    ]));
}

// POST-Daten empfangen
$data = json_decode(file_get_contents('php://input'), true);

// SQL-Abfrage vorbereiten
$sql = "SELECT * FROM ai_models WHERE 1=1";
$params = array();
$types = "";

// Name Filter
if (!empty($data['name'])) {
    $sql .= " AND Name LIKE ?";
    $params[] = "%" . $data['name'] . "%";
    $types .= "s";
}

// Kostenmodell Filter
if (!empty($data['price'])) {
    $sql .= " AND Kostenmodell = ?";
    $params[] = $data['price'];
    $types .= "s";
}

// Bewertung Filter
if (!empty($data['ranking'])) {
    $sql .= " AND Bewertung >= ?";
    $params[] = $data['ranking'];
    $types .= "i";
}

// Zielgruppe Filter
if (!empty($data['targetGroup'])) {
    $sql .= " AND Zielgruppe = ?";
    $params[] = $data['targetGroup'];
    $types .= "s";
}

// Prepared Statement erstellen
$stmt = $conn->prepare($sql);

// Parameter binden, falls vorhanden
if (!empty($params)) {
    $stmt->bind_param($types, ...$params);
}

// Abfrage ausführen
$stmt->execute();
$result = $stmt->get_result();

// Ergebnisse in Array umwandeln
$ais = array();
while ($row = $result->fetch_assoc()) {
    $ais[] = array(
        'id' => $row['ID'],
        'name' => $row['Name'],
        'price' => $row['Kostenmodell'],
        'rating' => $row['Bewertung'],
        'target_group' => $row['Zielgruppe'],
        'link' => $row['Aktion']
    );
}

// Verbindung schließen
$stmt->close();
$conn->close();

// Ergebnisse zurückgeben
echo json_encode([
    'success' => true,
    'ais' => $ais
]);
?> 