from tender_assistant import choisir_dossier, obtenir_tache


def test_obtenir_tache_retourne_les_trois_modes_connus():
    assert obtenir_tache("consultation") is not None
    assert obtenir_tache("entreprise") is not None
    assert obtenir_tache("comparaison") is not None


def test_obtenir_tache_retourne_none_pour_un_mode_inconnu():
    assert obtenir_tache("inconnu") is None


def test_choisir_dossier_trie_et_retourne_le_dossier_selectionne(
    tmp_path,
    monkeypatch,
):
    (tmp_path / "zeta").mkdir()
    (tmp_path / "alpha").mkdir()

    monkeypatch.setattr("builtins.input", lambda _: "1")

    resultat = choisir_dossier(tmp_path, "Dossiers de test")

    assert resultat == tmp_path / "alpha"
