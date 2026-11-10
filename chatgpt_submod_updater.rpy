# Register Submod Updater Plugin support

init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="ChatGPT Submod Five Linux Distros Dialogues",
            user_name="Kapiqiano7",
            repository_name="ChatGPT-Submod",
            tag_formatter=lambda tag: tag.lstrip("v")
        )
