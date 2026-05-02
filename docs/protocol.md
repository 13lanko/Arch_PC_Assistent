Das Meta Ziel dieses Projects ist es, eine Pipeline zu entwickeln, mit der kleineren Modell local oder über Cloud-Dienst zu einem Assistent des lokalen Rechners trainiert werden können. Es handelt es sich hauptsächlich um ein Finetuning eines vorab trainierten Modells mittels PEFT und GRPO. 

Bei meiner Projekt-Ausführung liegt der Fokus auf der Arch-Linux-Distribution mit dem Tiling-Window-Manager Hyprland, da dieses Setup meinem lokalen Rechner entspricht. 

Hierbei wird ein Docker-Container verwendet, sowie ein Paketmanager uv. Dadurch lässt sich das Projekt auf jedem Rechner ausführen und. Ebenso wird die Verwendung eines Cloud-Dienstes für das Trainieren des Modells möglich.

Ich habe mich für das vorab trainierte Modell „qwen2.5-7b-instruct-unsloth-bnb-4bit“ entschieden, da dieses von unsloth unterstützt wird und eine deutlich bessere Performance während des Trainings und der Antwortgenerierung zeigt. Die 4-Bit-Quatisierung erlaubt es, dieses Modell auf fast allen modernen GPUs auszuführen. Ein Ersatz diesen Modell ist flexibe solange es mit unsloth compatibel ist, da das ganze Pipeline auf der unsloth basiert.

Die Wahl von GRPO und PEFT mit LoRa als Hauptmethode des Feintunings wurde mit folgender Absicht getroffen: Mit LoRa lässt sich das Modell fast ohne Performanceverlust viel effizienter trainieren. Mit GRPO lässt sich das Modell das Reasoning-Funktion erlernen, was, wie bereits von DeepSeak R1 gezeigt wurde, eine enorme Leistungssteigerung für das Modell darstellt.

Zur Vorbereitung der ersten Phase sollte eine API mit einem starken Reasoning-Modell bereitgestellt werden, um daraus die Reasoning-Dataset zu destillieren. Für die Destillation sollte das Modell aus Rohdaten aus unterschiedlichen Dokumentationen, einschließlich Arch-Wiki, GitHub und Hyprland-Wiki, Datensätze erzeugen, damit die Datensätze aktuell bleiben und die Halluzinationsgefahr des Modells verhindert wird, auch wenn das Modell bereits eine enorme Genauigkeit hat. 

Da dem Modell nicht nur Fakten, sondern auch Reasoning-Muster beigebracht werden sollen, sollte es eine bestimmte Formatierung annehmen, die bei der Generalisierung der Datensätze berücksichtigt wird. Dafür wird eine Python-Code-Vorlage entworfen, mit der sich durch Wechsel der Raw-Dataset-Quelle und des API-Keys sowie der Beschreibung der Prompt-Datensätze beliebige Datensätze nach eigene Wunsch destillieren lassen. Diese validiert man anschließend, damit es wirklich als Goldstandard-Datensatz gilt.

