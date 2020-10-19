#Noah Telerman
#19/10/20

#Script to auto-run parameter optimization experiemtns on the Monaco laser

import Monaco
import PatchClamp

monaco = Monaco()
patch = PatchClamp()

monaco.power_on()

for i in len(experiment_values):
    monaco.set_parameters(experiment_values[i])
    monaco.run()
    patch.record()

monaco.power_off
