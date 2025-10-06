--1
SELECT posizione AS Fascia, COUNT(*) AS Numero_Strutturati
FROM Persona
GROUP BY posizione;
--2
SELECT COUNT(*) AS Numero_Strutturati
FROM Persona
WHERE stipendio >= 40000;
--3
SELECT COUNT(*) AS Numero_Progetti
FROM Progetto
WHERE fine < CURRENT_DATE
  AND budget > 50000;
--4
SELECT 
    AVG(oreDurata) AS Media_Ore,
    MAX(oreDurata) AS Massimo_Ore,
    MIN(oreDurata) AS Minimo_Ore
FROM AttivitaProgetto
WHERE progetto = (
    SELECT id 
    FROM Progetto
    WHERE nome = 'Pegasus'
);
--5
SELECT 
    persona AS Docente,
    AVG(ore_giornaliere) AS Media_Ore,
    MAX(ore_giornaliere) AS Massimo_Ore,
    MIN(ore_giornaliere) AS Minimo_Ore
FROM (
    SELECT 
        persona,
        giorno,
        SUM(oreDurata) AS ore_giornaliere
    FROM AttivitaProgetto
    WHERE progetto = (SELECT id FROM Progetto WHERE nome = 'Pegasus')
    GROUP BY persona, giorno
) AS giornate
GROUP BY persona
ORDER BY persona;


