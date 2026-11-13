from project import load_notes, split_into_chunks, rank_chunks, build_prompt, is_relevant, evaluate
import pytest

def test_load_notes(tmp_path):
    (tmp_path / "semana1.md").write_text("## Variaveis\nTexto da aula 1")
    (tmp_path / "semana2.md").write_text("## Funcoes\nTexto da aula 2")

    notes = load_notes(tmp_path) 

    assert len(notes) == 2
    assert set([n["source"] for n in notes]) == {"semana1.md", "semana2.md"}

def test_load_notes_pasta_inexistente(tmp_path):
    with pytest.raises(SystemExit):
        load_notes(tmp_path / "nao_existe")

def test_load_notes_pasta_vazia(tmp_path):
    with pytest.raises(SystemExit):
        load_notes(tmp_path)

def test_split_into_chunks_secoes():
    texto = "## Variaveis\nTexto 1\n\n## Funcoes\nTexto 2\n\n## Loops\nTexto 3"
    chunks = split_into_chunks(texto, "semana1.md")
    assert len(chunks) == 3
    assert chunks[0]["source"] == "semana1.md"
    assert chunks[0]["section"] == "Variaveis"
    assert chunks[0]["text"] == "Texto 1"

def test_split_into_chunks_overlap():
    p1 = "A" * 200
    p2 = "B" * 200
    p3 = "C" * 200
    texto = f"## Secao longa\n{p1}\n\n{p2}\n\n{p3}\n\n"
    chunks = split_into_chunks(texto, "semana1.md")
    assert len(chunks) == 2
    assert p2 in chunks[0]["text"]
    assert p2 in chunks[1]["text"]

def test_rank_chunks():
    chunks = [
    {"source": "aula0.md", "section": "Variaveis", "text": "Variaveis guardam valores int e str na memoria"},
    {"source": "aula4.md", "section": "Bibliotecas", "text": "Usamos import random e sys.argv para argumentos"},
    {"source": "aula8.md", "section": "POO", "text": "Classes, objetos, heranca e polimorfismo em Python"}]
    resultado = rank_chunks("o que eh polimorfismo e heranca?", chunks, k=2)
    assert len(resultado) == 2
    assert resultado[0]["source"] == "aula8.md"
    assert resultado[0]["score"] > resultado[1]["score"]

def build_prompt():
    chunks = [
        {"source": "aula0.md", "section": "Variaveis", "text": "Variaveis guardam valores int e str na memoria"},
        {"source": "aula4.md", "section": "Bibliotecas", "text": "Usamos import random e sys.argv para argumentos"},]
    question = "Para que servem as bibliotecas em python"
    prompt = build_prompt(question, chunks)

    assert "somente os trechos" in prompt
    assert "<trechos>" in prompt
    assert "</trechos>" in prompt
    assert '[1] aula0.md > Variaveis: "Caixas de memoria"' in prompt
    assert "Pergunta: O que sao variaveis? " in prompt

def test_is_relevant():
    # Cenário 1: Maior score (0.4) acima do limiar padrão (0.1) -> Deve ser True
    resultados_altos = [{"score": 0.4}, {"score": 0.1}]
    assert is_relevant(resultados_altos) == True

    # Cenário 2: Maior score (0.05) abaixo do limiar padrão (0.1) -> Deve ser False
    resultados_baixos = [{"score": 0.05}, {"score": 0.01}]
    assert is_relevant(resultados_baixos) == False

    # Cenário 3: Exatamente no limiar (0.1 >= 0.1) -> Deve ser True
    resultados_borda = [{"score": 0.1}]
    assert is_relevant(resultados_borda, threshold=0.1) == True

    # Cenário 4: Lista vazia (proteção contra erro de índice) -> Deve ser False
    assert is_relevant([]) == False

def test_evaluate():
    chunks = [
        {"source": "aula0.md", "section": "Variaveis", "text": "Variaveis guardam valores int e str na memoria"},
        {"source": "aula4.md", "section": "Bibliotecas", "text": "Usamos import random e sys.argv para argumentos"},
        {"source": "aula8.md", "section": "POO", "text": "Classes, objetos, heranca e polimorfismo em Python"}]

    cases_100 = [
        {"question": "O que são variáveis?", "expected_source": "aula0.md"},
        {"question": "O que são bibliotecas?", "expected_source": "aula4.md"}
    ]

    cases_50 = [
            {"question": "O que são variáveis?", "expected_source": "aula0.md"},
            {"question": "O que são bibliotecas?", "expected_source": "aula99.md"}
        ]

    assert evaluate(chunks, cases_100) == 1.0
    assert evaluate(chunks, cases_50) == 0.5
    assert (evaluate(chunks, []) == 0)