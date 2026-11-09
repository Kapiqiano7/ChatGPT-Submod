# Register ChatGPT Linux Distros Submod

init -990 python:
    store.mas_submod_utils.Submod(
        author="Kapiqiano",
        name="ChatGPT Submod Five Linux Distros Dialogues",
        description="Five English conversations about Ubuntu, Arch Linux, Fedora, Linux Mint, and Debian.",
        version="1.0.2"
    )
# Register Submod Updater Plugin support

init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="ChatGPT Submod Five Linux Distros Dialogues",
            user_name="Kapiqiano7",
            repository_name="ChatGPT-Submod",
            tag_formatter=lambda tag: tag.lstrip("v")
        )
