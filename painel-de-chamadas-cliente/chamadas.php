<?php
// Conectar ao banco de dados SQLite
try {
    $pdo = new PDO('sqlite:C:\xampp\htdocs\chamadas.db');
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    echo json_encode(['error' => "Erro na conexão com o banco de dados: " . $e->getMessage()]);
    exit();
}

// Função para buscar os registros mais recentes por unidade
function buscarChamadasRecentes($pdo) {
    $stmt = $pdo->query('
        SELECT c1.*
        FROM chamadas c1
        INNER JOIN (
            SELECT nome_unidade, MAX(id) as max_id
            FROM chamadas
            GROUP BY nome_unidade
        ) c2
        ON c1.id = c2.max_id
        ORDER BY c1.id DESC
        LIMIT 3
    ');
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

// Buscar chamadas recentes
$chamadas = buscarChamadasRecentes($pdo);

// Retornar as chamadas como JSON
header('Content-Type: application/json');
echo json_encode($chamadas);
?>
