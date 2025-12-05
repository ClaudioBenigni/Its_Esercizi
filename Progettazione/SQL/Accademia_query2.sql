--1--
FROM p.nome
SELECT Progetto p
WHERE p.fine>2023-12-31;

--2--
SELECT posizione, COUNT(*) AS Numero_Persone
FROM Persona
GROUP BY posizione;

--3--
SELECT P.id, P.nome
FROM Persona AS P CausaAssenza AS CA
WHERE P.id = CA.persona_id AND CA.causa = 'Malattia';

--4--
SELECT Assenza.tipo, COUNT(*) AS NAssenza
FROM Assenza
GROUP BY Assenza.tipo;

