# ChatGPT Submod - Five Linux Distros Dialogues
# Registers five player-initiated Linux conversation topics.

init 5 python:

    addEvent(Event(
        persistent.event_database,
        eventlabel="monika_kapiqiano_linux_ubuntu",
        category=["technology"],
        prompt="Can we talk about Ubuntu?",
        unlocked=True,
        random=False,
        pool=True,
        rules={"no_unlock": None}
    ))

    addEvent(Event(
        persistent.event_database,
        eventlabel="monika_kapiqiano_linux_arch",
        category=["technology"],
        prompt="Can we talk about Arch Linux?",
        unlocked=True,
        random=False,
        pool=True,
        rules={"no_unlock": None}
    ))

    addEvent(Event(
        persistent.event_database,
        eventlabel="monika_kapiqiano_linux_fedora",
        category=["technology"],
        prompt="Can we talk about Fedora?",
        unlocked=True,
        random=False,
        pool=True,
        rules={"no_unlock": None}
    ))

    addEvent(Event(
        persistent.event_database,
        eventlabel="monika_kapiqiano_linux_mint",
        category=["technology"],
        prompt="Can we talk about Linux Mint?",
        unlocked=True,
        random=False,
        pool=True,
        rules={"no_unlock": None}
    ))

    addEvent(Event(
        persistent.event_database,
        eventlabel="monika_kapiqiano_linux_debian",
        category=["technology"],
        prompt="Can we talk about Debian?",
        unlocked=True,
        random=False,
        pool=True,
        rules={"no_unlock": None}
    ))