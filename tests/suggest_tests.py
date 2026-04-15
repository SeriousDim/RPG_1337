from view.classical_user_study.suggest import get_leaf_subfolders, prepare_selection


dirs = get_leaf_subfolders("./view/resources/quests")
indices = prepare_selection(dirs)

for i in indices:
    print(dirs[i])
