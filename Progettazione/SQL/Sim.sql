SELECT persona.posizione, COUNT(persona.posizione) as Numero_Totale
FROM persona 
GROUP BY persona.posizione;


SELECT COUNT(persona.stipendio) as stipendio
from persona
where stipendio >=40000;


SELECT COUNT(Progetto.id) as soldi
from Progetto
where CURRENT_DATE>progetto.fine and progetto.budget > 50000;

SELECT AVG(AttivitaProgetto.oreDurata), MAX(AttivitaProgetto.oreDurata), MIN(AttivitaProgetto.oreDurata)
from progetto,AttivitaProgetto
where AttivitaProgetto.progetto=progetto.id and progetto.nome="Pegasus"; 

SELECT persona.nome,persona.cognome, AVG(AttivitaProgetto.oreDurata), MAX(AttivitaProgetto.oreDurata), MIN(AttivitaProgetto.oreDurata)
from persona,AttivitaProgetto,progetto
where progetto.nome='Pegasus' and persona.posizione='Professore Ordinario' and persona.id =AttivitaProgetto.persona
GROUP BY persona.nome,persona.cognome;