#------------------------------------------------------------------------------
# Description    : Pulsar QRM QCoDeS interface
# Git repository : https://gitlab.com/qblox/packages/software/qblox_instruments.git
# Copyright (C) Qblox BV (2020)
#------------------------------------------------------------------------------


#-- include -------------------------------------------------------------------

from ieee488_2.transport       import ip_transport, pulsar_dummy_transport
from pulsar_qrm.pulsar_qrm_ifc import pulsar_qrm_ifc
from qcodes                    import validators as vals
from qcodes                    import Instrument
from jsonschema                import validate
from functools                 import partial
import json

#-- class ---------------------------------------------------------------------

class pulsar_qrm_qcodes(pulsar_qrm_ifc, Instrument):
    """
    This class connects `QCoDeS <https://qcodes.github.io/Qcodes/>`_ to the Pulsar QRM native interface. Do not directly instantiate this class, but instead instantiate either the
    :class:`~.pulsar_qrm` or :class:`~.pulsar_qrm_dummy`.
    """

    #--------------------------------------------------------------------------
    def __init__(self, name, transport_inst, debug=0):
        """
        Creates Pulsar QRM QCoDeS class and adds all relevant instrument parameters. These instrument parameters call the associated methods provided by the native interface.

        Parameters
        ----------
        name : str
            Instrument name.
        transport_inst : :class:`~ieee488_2.transport`
            Transport class responsible for the lowest level of communication (e.g. ethernet).
        debug : int
            Debug level (0 = normal, 1 = no version check, >1 = no version or error checking).

        Returns
        ----------

        Raises
        ----------
        Exception
            Debug level is 0 and there is a version mismatch.


        .. Note::

            To get a complete of list of the QCoDeS parameters, run the following code.

        .. code-block:: Python

            from pulsar_qrm.pulsar_qrm import pulsar_qrm_dummy

            qrm = pulsar_qrm_dummy("qrm")
            for call in qrm.snapshot()['parameters']:
                print(getattr(qrm, call).__doc__)
        """

        #Initialize parent classes.
        super(pulsar_qrm_qcodes, self).__init__(transport_inst, debug)
        Instrument.__init__(self, name)

        #Set instrument parameters
        self._num_sequencers = 6

        #Set JSON schema to validate JSON file with
        self._wave_and_prog_json_schema = {"title":       "Sequencer waveforms and program container",
                                           "description": "Contains both all waveforms, weights and acquisitions and a program required for a sequence.",
                                           "type":        "object",
                                           "required":    ["program", "waveforms", "weights", "acquisitions"],
                                           "properties": {
                                               "program": {
                                                   "description": "Sequencer assembly program in string format.",
                                                   "type":        "string"
                                               },
                                               "waveforms": {
                                                   "description": "Waveform dictionary containing one or multiple AWG waveform(s).",
                                                   "type":        "object",
                                               },
                                               "weights": {
                                                   "description": "Weight dictionary containing one or multiple acquisition weights(s).",
                                                   "type":        "object",
                                               },
                                               "acquisitions": {
                                                   "description": "Acquisition dictionary containing information about one or multiple acquisition(s).",
                                                   "type":        "object"
                                               }
                                           }}
        self._wave_json_schema = {"title":       "Waveform/weight container",
                                  "description": "Waveform/weight dictionary for a single waveform.",
                                  "type":        "object",
                                  "required":    ["data"],
                                  "properties": {
                                      "data":  {
                                          "description": "List of waveform samples.",
                                          "type":        "array"
                                      },
                                      "index": {
                                          "description": "Optional waveform index number.",
                                          "type":        "number"
                                      }
                                  }}

        self._acq_json_schema = {"title":       "Acquisition container",
                                 "description": "Acquisition dictionary for a single acquisition.",
                                 "type":        "object",
                                 "required":    ["num_bins"],
                                 "properties": {
                                     "num_bins": {
                                         "description": "Number of bins in acquisition.",
                                         "type":        "number"
                                     },
                                     "index": {
                                         "description": "Optional waveform index number.",
                                         "type":        "number"
                                     }
                                 }}

        #Add QCoDeS parameters
        self.add_parameter(
            "reference_source",
            label       = "Reference source.",
            docstring   = "Sets/gets reference source ('internal' = internal 10 MHz, 'external' = external 10 MHz).",
            unit        = '',
            vals        = vals.Bool(),
            val_mapping = {"internal": True, "external": False},
            set_parser  = bool,
            get_parser  = bool,
            set_cmd     = self._set_reference_source,
            get_cmd     = self._get_reference_source
        )

        if self._get_lo_hw_present():
            self.add_parameter(
                "out0_in0_lo_freq",
                label      = "Local Oscillator frequency for output 0 and input 0.",
                docstring  = "Sets/gets the local oscillator frequency for output 0 and input 0.",
                unit       = 'Hz',
                vals       = vals.Numbers(2e9, 18e9),
                set_parser = int,
                get_parser = int,
                set_cmd    = self._set_lo_freq_1,
                get_cmd    = self._get_lo_freq_1
            )

        if not self._get_lo_hw_present():
            self.add_parameter(
                "in0_gain",
                label      = "Input 0 gain.",
                docstring  = "Sets/gets input 0 gain in a range of -6dB to 26dB with a resolution of 1dB per step.",
                unit       = 'dB',
                vals       = vals.Numbers(-6, 26),
                set_parser = int,
                get_parser = int,
                set_cmd    = self._set_in_amp_gain_0,
                get_cmd    = self._get_in_amp_gain_0
            )

            self.add_parameter(
                "in1_gain",
                label      = "Input 1 gain.",
                docstring  = "Sets/gets input 1 gain in a range of -6dB to 26dB with a resolution of 1dB per step.",
                unit       = 'dB',
                vals       = vals.Numbers(-6, 26),
                set_parser = int,
                get_parser = int,
                set_cmd    = self._set_in_amp_gain_1,
                get_cmd    = self._get_in_amp_gain_1
            )

        if self._get_lo_hw_present():
            self.add_parameter(
                "out0_offset_path0",
                label      = "Output 0 offset for path 0.",
                docstring  = "Sets/gets output 0 offset for path 0.",
                unit       = 'mV',
                vals       = vals.Numbers(-84.0, 73.0),
                set_parser = float,
                get_parser = float,
                set_cmd    = self._set_out_amp_offset_0,
                get_cmd    = self._get_out_amp_offset_0
            )

            self.add_parameter(
                "out0_offset_path1",
                label      = "Output 0 offset for path 1.",
                docstring  = "Sets/gets output 0 offset for path 1.",
                unit       = 'mV',
                vals       = vals.Numbers(-84.0, 73.0),
                set_parser = float,
                get_parser = float,
                set_cmd    = self._set_out_amp_offset_1,
                get_cmd    = self._get_out_amp_offset_1
            )
        else:
            self.add_parameter(
                "out0_offset",
                label      = "Output 0 offset.",
                docstring  = "Sets/gets output 0 offset.",
                unit       = 'V',
                vals       = vals.Numbers(-1.0, 1.0),
                set_parser = float,
                get_parser = float,
                set_cmd    = self._set_dac_offset_0,
                get_cmd    = self._get_dac_offset_0
            )

            self.add_parameter(
                "out1_offset",
                label      = "Output 1 offset.",
                docstring  = "Sets/gets output 1 offset.",
                unit       = 'V',
                vals       = vals.Numbers(-1.0, 1.0),
                set_parser = float,
                get_parser = float,
                set_cmd    = self._set_dac_offset_1,
                get_cmd    = self._get_dac_offset_1
            )

        #--Scope acquisition settings------------------------------------------
        self.add_parameter(
            "scope_acq_trigger_mode_path0",
            label       = "Scope acquisition trigger mode for input path 0.",
            docstring   = "Sets/gets scope acquisition trigger mode for input path 0 ('sequencer' = triggered by sequencer, 'level' = triggered by input level).",
            unit        = '',
            vals        = vals.Bool(),
            val_mapping = {"level": True, "sequencer": False},
            set_parser  = bool,
            get_parser  = bool,
            set_cmd     = partial(self._set_acq_scope_config_val, "trig_mode_acq_path_0"),
            get_cmd     = partial(self._get_acq_scope_config_val, "trig_mode_acq_path_0")
        )

        self.add_parameter(
            "scope_acq_trigger_mode_path1",
            label       = "Scope acquisition trigger mode for input path 0.",
            docstring   = "Sets/gets scope acquisition trigger mode for input path 1 ('sequencer' = triggered by sequencer, 'level' = triggered by input level).",
            unit        = '',
            vals        = vals.Bool(),
            val_mapping = {"level": True, "sequencer": False},
            set_parser  = bool,
            get_parser  = bool,
            set_cmd     = partial(self._set_acq_scope_config_val, "trig_mode_acq_path_1"),
            get_cmd     = partial(self._get_acq_scope_config_val, "trig_mode_acq_path_1")
        )

        self.add_parameter(
            "scope_acq_trigger_level_path0",
            label      = "Scope acquisition trigger level when using input level trigger mode for input path 0.",
            docstring  = "Sets/gets scope acquisition trigger level when using input level trigger mode for input path 0.",
            unit       = '',
            vals       = vals.Numbers(-1.0, 1.0),
            set_parser = float,
            get_parser = float,
            set_cmd    = partial(self._set_acq_scope_config_val, "trig_lvl_acq_path_0_float"),
            get_cmd    = partial(self._get_acq_scope_config_val, "trig_lvl_acq_path_0_float")
        )

        self.add_parameter(
            "scope_acq_trigger_level_path1",
            label      = "Scope acquisition trigger level when using input level trigger mode for input path 1.",
            docstring  = "Sets/gets scope acquisition trigger level when using input level trigger mode for input path 1.",
            unit       = '',
            vals       = vals.Numbers(-1.0, 1.0),
            set_parser = float,
            get_parser = float,
            set_cmd    = partial(self._set_acq_scope_config_val, "trig_lvl_acq_path_1_float"),
            get_cmd    = partial(self._get_acq_scope_config_val, "trig_lvl_acq_path_1_float")
        )

        self.add_parameter(
            "scope_acq_sequencer_select",
            label       = "Scope acquisition sequencer select for when using sequencer trigger mode.",
            docstring   = "Sets/gets sequencer select that specifies which sequencer triggers the scope acquisition when using sequencer trigger mode.",
            unit        = '',
            vals        = vals.Numbers(0, self._num_sequencers),
            set_parser  = int,
            get_parser  = int,
            set_cmd     = partial(self._set_acq_scope_config_val, "sel_acq"),
            get_cmd     = partial(self._get_acq_scope_config_val, "sel_acq")
        )

        self.add_parameter(
            "scope_acq_avg_mode_en_path0",
            label      = "Scope acquisition averaging mode enable for input path 0.",
            docstring  = "Sets/gets scope acquisition averaging mode enable for input path 0.",
            unit       = '',
            vals       = vals.Bool(),
            set_parser = bool,
            get_parser = bool,
            set_cmd    = partial(self._set_acq_scope_config_val, "avg_en_acq_path_0"),
            get_cmd    = partial(self._get_acq_scope_config_val, "avg_en_acq_path_0")
        )
        self.add_parameter(
            "scope_acq_avg_mode_en_path1",
            label      = "Scope acquisition averaging mode enable for input path 0.",
            docstring  = "Sets/gets scope acquisition averaging mode enable for input path 0.",
            unit       = '',
            vals       = vals.Bool(),
            set_parser = bool,
            get_parser = bool,
            set_cmd    = partial(self._set_acq_scope_config_val, "avg_en_acq_path_1"),
            get_cmd    = partial(self._get_acq_scope_config_val, "avg_en_acq_path_1")
        )

        for seq_idx in range(0, self._num_sequencers):
            #--Sequencer settings----------------------------------------------
            self.add_parameter(
                "sequencer{}_channel_map_path0_out0_en".format(seq_idx),
                label      = "Sequencer {} path 0 output 0 enable.".format(seq_idx),
                docstring  = "Sets/gets sequencer {} channel map enable of path 0 to output 0.".format(seq_idx),
                unit       = '',
                vals       = vals.Bool(),
                set_parser = bool,
                get_parser = bool,
                set_cmd    = partial(self._set_sequencer_channel_map, seq_idx, 0),
                get_cmd    = partial(self._get_sequencer_channel_map, seq_idx, 0)
            )

            self.add_parameter(
                "sequencer{}_channel_map_path1_out1_en".format(seq_idx),
                label      = "Sequencer {} path 1 output 1 enable.".format(seq_idx),
                docstring  = "Sets/gets sequencer {} channel map enable of path 1 to output 1.".format(seq_idx),
                unit       = '',
                vals       = vals.Bool(),
                set_parser = bool,
                get_parser = bool,
                set_cmd    = partial(self._set_sequencer_channel_map, seq_idx, 1),
                get_cmd    = partial(self._get_sequencer_channel_map, seq_idx, 1)
            )
            self.add_parameter(
                "sequencer{}_sync_en".format(seq_idx),
                label      = "Sequencer {} synchronization enable which enables party-line synchronization.".format(seq_idx),
                docstring  = "Sets/gets sequencer {} synchronization enable which enables party-line synchronization.".format(seq_idx),
                unit       = '',
                vals       = vals.Bool(),
                set_parser = bool,
                get_parser = bool,
                set_cmd    = partial(self._set_sequencer_config_val, seq_idx, "sync_en"),
                get_cmd    = partial(self._get_sequencer_config_val, seq_idx, "sync_en")
            )

            self.add_parameter(
                "sequencer{}_nco_freq".format(seq_idx),
                label      = "Sequencer {} NCO frequency.".format(seq_idx),
                docstring  = "Sets/gets sequencer {} NCO frequency in Hz with a resolution of 0.25 Hz.".format(seq_idx),
                unit       = 'Hz',
                vals       = vals.Numbers(-300e6, 300e6),
                set_parser = float,
                get_parser = float,
                set_cmd    = partial(self._set_sequencer_config_val, seq_idx, "freq_hz"),
                get_cmd    = partial(self._get_sequencer_config_val, seq_idx, "freq_hz")
            )

            self.add_parameter(
                "sequencer{}_nco_phase_offs".format(seq_idx),
                label      = "Sequencer {} NCO phase offset.".format(seq_idx),
                docstring  = "Sets/gets sequencer {} NCO phase offset in degrees with a resolution of 3.6e-7 degrees.".format(seq_idx),
                unit       = 'Degrees',
                vals       = vals.Numbers(0, 360),
                set_parser = float,
                get_parser = float,
                set_cmd    = partial(self._set_sequencer_config_val, seq_idx, "phase_offs_degree"),
                get_cmd    = partial(self._get_sequencer_config_val, seq_idx, "phase_offs_degree")
            )

            self.add_parameter(
                "sequencer{}_marker_ovr_en".format(seq_idx),
                label      = "Sequencer {} marker override enable.".format(seq_idx),
                docstring  = "Sets/gets sequencer {} marker override enable.".format(seq_idx),
                unit       = '',
                vals       = vals.Bool(),
                set_parser = bool,
                get_parser = bool,
                set_cmd    = partial(self._set_sequencer_config_val, seq_idx, "mrk_ovr_en"),
                get_cmd    = partial(self._get_sequencer_config_val, seq_idx, "mrk_ovr_en")
            )

            self.add_parameter(
                "sequencer{}_marker_ovr_value".format(seq_idx),
                label      = "Sequencer {} marker override value.".format(seq_idx),
                docstring  = "Sets/gets sequencer {} marker override value. Bit index corresponds to marker channel index.".format(seq_idx),
                unit       = '',
                vals       = vals.Numbers(0, 15),
                set_parser = int,
                get_parser = int,
                set_cmd    = partial(self._set_sequencer_config_val, seq_idx, "mrk_ovr_val"),
                get_cmd    = partial(self._get_sequencer_config_val, seq_idx, "mrk_ovr_val")
            )

            self.add_parameter(
                "sequencer{}_waveforms_and_program".format(seq_idx),
                label      = "Sequencer {} AWG waveforms, acquistion weights, acquisitions and ASM program.".format(seq_idx),
                docstring  = "Sets sequencer {} AWG waveforms, acquistion weights, acquisitions and ASM program. Valid input is a string representing the JSON filename.".format(seq_idx),
                vals       = vals.Strings(),
                set_parser = str,
                get_parser = str,
                set_cmd    = partial(self._set_sequencer_waveforms_and_program, seq_idx),
            )



            #--AWG settings----------------------------------------------------
            self.add_parameter(
                "sequencer{}_cont_mode_en_awg_path0".format(seq_idx),
                label      = "Sequencer {} continous waveform mode enable for AWG path 0.".format(seq_idx),
                docstring  = "Sets/gets sequencer {} continous waveform mode enable for AWG path 0.".format(seq_idx),
                unit       = '',
                vals       = vals.Bool(),
                set_parser = bool,
                get_parser = bool,
                set_cmd    = partial(self._set_sequencer_config_val, seq_idx, "cont_mode_en_awg_path_0"),
                get_cmd    = partial(self._get_sequencer_config_val, seq_idx, "cont_mode_en_awg_path_0")
            )

            self.add_parameter(
                "sequencer{}_cont_mode_en_awg_path1".format(seq_idx),
                label      = "Sequencer {} continous waveform mode enable for AWG path 1.".format(seq_idx),
                docstring  = "Sets/gets sequencer {} continous waveform mode enable for AWG path 1.".format(seq_idx),
                unit       = '',
                vals       = vals.Bool(),
                set_parser = bool,
                get_parser = bool,
                set_cmd    = partial(self._set_sequencer_config_val, seq_idx, "cont_mode_en_awg_path_1"),
                get_cmd    = partial(self._get_sequencer_config_val, seq_idx, "cont_mode_en_awg_path_1")
            )

            self.add_parameter(
                "sequencer{}_cont_mode_waveform_idx_awg_path0".format(seq_idx),
                label      = "Sequencer {} continous waveform mode waveform index for AWG path 0.".format(seq_idx),
                docstring  = "Sets/gets sequencer {} continous waveform mode waveform index or AWG path 0.".format(seq_idx),
                unit       = '',
                vals       = vals.Numbers(0, 2**10-1),
                set_parser = int,
                get_parser = int,
                set_cmd    = partial(self._set_sequencer_config_val, seq_idx, "cont_mode_waveform_idx_awg_path_0"),
                get_cmd    = partial(self._get_sequencer_config_val, seq_idx, "cont_mode_waveform_idx_awg_path_0")
            )

            self.add_parameter(
                "sequencer{}_cont_mode_waveform_idx_awg_path1".format(seq_idx),
                label      = "Sequencer {} continous waveform mode waveform index for AWG path 1.".format(seq_idx),
                docstring  = "Sets/gets sequencer {} continous waveform mode waveform index or AWG path 1.".format(seq_idx),
                unit       = '',
                vals       = vals.Numbers(0, 2**10-1),
                set_parser = int,
                get_parser = int,
                set_cmd    = partial(self._set_sequencer_config_val, seq_idx, "cont_mode_waveform_idx_awg_path_1"),
                get_cmd    = partial(self._get_sequencer_config_val, seq_idx, "cont_mode_waveform_idx_awg_path_1")
            )

            self.add_parameter(
                "sequencer{}_upsample_rate_awg_path0".format(seq_idx),
                label      = "Sequencer {} upsample rate for AWG path 0.".format(seq_idx),
                docstring  = "Sets/gets sequencer {} upsample rate for AWG path 0.".format(seq_idx),
                unit       = '',
                vals       = vals.Numbers(0, 2**16-1),
                set_parser = int,
                get_parser = int,
                set_cmd    = partial(self._set_sequencer_config_val, seq_idx, "upsample_rate_awg_path_0"),
                get_cmd    = partial(self._get_sequencer_config_val, seq_idx, "upsample_rate_awg_path_0")
            )

            self.add_parameter(
                "sequencer{}_upsample_rate_awg_path1".format(seq_idx),
                label      = "Sequencer {} upsample rate for AWG path 1.".format(seq_idx),
                docstring  = "Sets/gets sequencer {} upsample rate for AWG path 1.".format(seq_idx),
                unit       = '',
                vals       = vals.Numbers(0, 2**16-1),
                set_parser = int,
                get_parser = int,
                set_cmd    = partial(self._set_sequencer_config_val, seq_idx, "upsample_rate_awg_path_1"),
                get_cmd    = partial(self._get_sequencer_config_val, seq_idx, "upsample_rate_awg_path_1")
            )

            self.add_parameter(
                "sequencer{}_gain_awg_path0".format(seq_idx),
                label      = "Sequencer {} gain for AWG path 0.".format(seq_idx),
                docstring  = "Sets/gets sequencer {} gain for AWG path 0.".format(seq_idx),
                unit       = '',
                vals       = vals.Numbers(-1.0, 1.0),
                set_parser = float,
                get_parser = float,
                set_cmd    = partial(self._set_sequencer_config_val, seq_idx, "gain_awg_path_0_float"),
                get_cmd    = partial(self._get_sequencer_config_val, seq_idx, "gain_awg_path_0_float")
            )

            self.add_parameter(
                "sequencer{}_gain_awg_path1".format(seq_idx),
                label      = "Sequencer {} gain for AWG path 1.".format(seq_idx),
                docstring  = "Sets/gets sequencer {} gain for AWG path 1.".format(seq_idx),
                unit       = '',
                vals       = vals.Numbers(-1.0, 1.0),
                set_parser = float,
                get_parser = float,
                set_cmd    = partial(self._set_sequencer_config_val, seq_idx, "gain_awg_path_1_float"),
                get_cmd    = partial(self._get_sequencer_config_val, seq_idx, "gain_awg_path_1_float")
            )

            self.add_parameter(
                "sequencer{}_offset_awg_path0".format(seq_idx),
                label      = "Sequencer {} offset for AWG path 0.".format(seq_idx),
                docstring  = "Sets/gets sequencer {} offset for AWG path 0.".format(seq_idx),
                unit       = '',
                vals       = vals.Numbers(-1.0, 1.0),
                set_parser = float,
                get_parser = float,
                set_cmd    = partial(self._set_sequencer_config_val, seq_idx, "offset_awg_path_0_float"),
                get_cmd    = partial(self._get_sequencer_config_val, seq_idx, "offset_awg_path_0_float")
            )

            self.add_parameter(
                "sequencer{}_offset_awg_path1".format(seq_idx),
                label      = "Sequencer {} offset for AWG path 1.".format(seq_idx),
                docstring  = "Sets/gets sequencer {} offset for AWG path 1.".format(seq_idx),
                unit       = '',
                vals       = vals.Numbers(-1.0, 1.0),
                set_parser = float,
                get_parser = float,
                set_cmd    = partial(self._set_sequencer_config_val, seq_idx, "offset_awg_path_1_float"),
                get_cmd    = partial(self._get_sequencer_config_val, seq_idx, "offset_awg_path_1_float")
            )

            self.add_parameter(
                "sequencer{}_mixer_corr_phase_offset_degree".format(seq_idx),
                label      = "Sequencer {} mixer phase imbalance correction for AWG; applied to AWG path 1 relative to AWG path 0 and measured in degrees.".format(seq_idx),
                docstring  = "Sets/gets sequencer {} mixer phase imbalance correction for AWG; applied to AWG path 1 relative to AWG path 0 and measured in degrees".format(seq_idx),
                unit       = '',
                vals       = vals.Numbers(-45.0, 45.0),
                set_parser = float,
                get_parser = float,
                set_cmd    = partial(self._set_sequencer_config_val, seq_idx, "mixer_corr_phase_offset_degree_float"),
                get_cmd    = partial(self._get_sequencer_config_val, seq_idx, "mixer_corr_phase_offset_degree_float")
            )

            self.add_parameter(
                "sequencer{}_mixer_corr_gain_ratio".format(seq_idx),
                label      = "Sequencer {} mixer gain imbalance correction for AWG; equal to AWG path 1 amplitude divided by AWG path 0 amplitude.".format(seq_idx),
                docstring  = "Sets/gets sequencer {} mixer gain imbalance correction for AWG; equal to AWG path 1 amplitude divided by AWG path 0 amplitude.".format(seq_idx),
                unit       = '',
                vals       = vals.Numbers(0.5, 2.0),
                set_parser = float,
                get_parser = float,
                set_cmd    = partial(self._set_sequencer_config_val, seq_idx, "mixer_corr_gain_ratio_float"),
                get_cmd    = partial(self._get_sequencer_config_val, seq_idx, "mixer_corr_gain_ratio_float")
            )

            self.add_parameter(
                "sequencer{}_mod_en_awg".format(seq_idx),
                label      = "Sequencer {} modulation enable for AWG.".format(seq_idx),
                docstring  = "Sets/gets sequencer {} modulation enable for AWG.".format(seq_idx),
                unit       = '',
                vals       = vals.Bool(),
                set_parser = bool,
                get_parser = bool,
                set_cmd    = partial(self._set_sequencer_config_val, seq_idx, "mod_en_awg"),
                get_cmd    = partial(self._get_sequencer_config_val, seq_idx, "mod_en_awg")
            )



            #--Acquisition settings--------------------------------------------
            self.add_parameter(
                "sequencer{}_demod_en_acq".format(seq_idx),
                label      = "Sequencer {} demodulation enable for acquisition.".format(seq_idx),
                docstring  = "Sets/gets sequencer {} demodulation enable for acquisition.".format(seq_idx),
                unit       = '',
                vals       = vals.Bool(),
                set_parser = bool,
                get_parser = bool,
                set_cmd    = partial(self._set_sequencer_config_val, seq_idx, "demod_en_acq"),
                get_cmd    = partial(self._get_sequencer_config_val, seq_idx, "demod_en_acq")
            )

            self.add_parameter(
                "sequencer{}_integration_length_acq".format(seq_idx),
                label      = "Sequencer {} integration length for acquisition paths 0 and 1".format(seq_idx),
                docstring  = "Sets/gets sequencer {} integration length in number of samples for non-weighed acquisitions on paths 0 and 1. Must be a multiple of 4".format(seq_idx),
                unit       = '',
                vals       = vals.Multiples(4, min_value=4, max_value=2**24-4),
                set_parser = int,
                get_parser = int,
                set_cmd    = partial(self._set_sequencer_config_val, seq_idx, "non_weighed_integration_len"),
                get_cmd    = partial(self._get_sequencer_config_val, seq_idx, "non_weighed_integration_len")
            )

            self.add_parameter(
                "sequencer{}_phase_rotation_acq".format(seq_idx),
                label      = "Sequencer {} integration result phase rotation".format(seq_idx),
                docstring  = "Sets/gets sequencer {} integration result phase rotation in degrees.".format(seq_idx),
                unit       = 'Degrees',
                vals       = vals.Numbers(0, 360),
                set_parser = float,
                get_parser = float,
                set_cmd    = partial(self._set_sequencer_config_rotation_matrix, seq_idx),
                get_cmd    = partial(self._get_sequencer_config_rotation_matrix, seq_idx)
            )

            self.add_parameter(
                "sequencer{}_discretization_threshold_acq".format(seq_idx),
                label      = "Sequencer {} discretization threshold".format(seq_idx),
                docstring  = "Sets/gets sequencer {} discretization threshold for discretizing the phase rotation result. ".format(seq_idx) + \
                             "Discretization is done by comparing the threshold to the rotated integration result of path 0. " + \
                             "This comparison is applied before normalization (i.e. division) of the rotated value " + \
                             "with the integration length and therefore the threshold needs to be compensated " + \
                             "(i.e. multiplied) with this length for the discretization to function properly.",
                unit       = '',
                vals       = vals.Numbers(-1.0*(2**24-4), 1.0*(2**24-4)),
                set_parser = float,
                get_parser = float,
                set_cmd    = partial(self._set_sequencer_config_val, seq_idx, "discr_threshold"),
                get_cmd    = partial(self._get_sequencer_config_val, seq_idx, "discr_threshold")
            )

    #--------------------------------------------------------------------------
    def _invalidate_qcodes_parameter_cache(self):
        """
        Marks the cache of all qcodes parameters on this instrument as invalid.
        """
        instrument_parameters = self.parameters.values()
        for parameter in instrument_parameters:
            parameter.cache.invalidate()

    #--------------------------------------------------------------------------
    def reset(self):
        """
        Resets device, invalidates QCoDeS parameter cache and clears all status and event registers (see `SCPI <https://www.ivifoundation.org/docs/scpi-99.pdf>`_).

        Parameters
        ----------

        Returns
        ----------

        Raises
        ----------
        Exception
            An error is reported in system error and debug <= 1.
            All errors are read from system error and listed in the exception.
        """
        self._invalidate_qcodes_parameter_cache()
        super().reset()

    #--------------------------------------------------------------------------
    def _set_acq_scope_config_val(self, param, val):
        """
        Set value of specific scope acquisition parameter.

        Parameters
        ----------
        param : str
            Parameter name.
        val
            Value to set parameter to.

        Returns
        ----------

        Raises
        ----------
        Exception
            Invalid input parameter type.
        Exception
            An error is reported in system error and debug <= 1.
            All errors are read from system error and listed in the exception.
        """

        self._set_acq_scope_config({param: val})

    #--------------------------------------------------------------------------
    def _get_acq_scope_config_val(self, param):
        """
        Get value of specific scope acquistion parameter.

        Parameters
        ----------
        param : str
            Parameter name.

        Returns
        ----------
        val
            Parameter value.

        Raises
        ----------
        Exception
            Invalid input parameter type.
        Exception
            An error is reported in system error and debug <= 1.
            All errors are read from system error and listed in the exception.
        """

        return self._get_acq_scope_config()[param]

    #--------------------------------------------------------------------------
    def _set_sequencer_config_val(self, sequencer, param, val):
        """
        Set value of specific sequencer parameter.

        Parameters
        ----------
        sequencer : int
            Sequencer index.
        param : str
            Parameter name.
        val
            Value to set parameter to.

        Returns
        ----------

        Raises
        ----------
        Exception
            Invalid input parameter type.
        Exception
            An error is reported in system error and debug <= 1.
            All errors are read from system error and listed in the exception.
        """

        self._set_sequencer_config(sequencer, {param: val})

    #--------------------------------------------------------------------------
    def _get_sequencer_config_val(self, sequencer, param):
        """
        Get value of specific sequencer parameter.

        Parameters
        ----------
        sequencer : int
            Sequencer index.
        param : str
            Parameter name.

        Returns
        ----------
        val
            Parameter value.

        Raises
        ----------
        Exception
            Invalid input parameter type.
        Exception
            An error is reported in system error and debug <= 1.
            All errors are read from system error and listed in the exception.
        """

        return self._get_sequencer_config(sequencer)[param]

    #--------------------------------------------------------------------------
    def _set_sequencer_waveforms_and_program(self, sequencer, file_name):
        """
        Set sequencer waveforms and program from JSON file. The JSON file needs to apply the schema specified by :member:`pulsar_qrm.pulsar_qrm_qcodes._wave_and_prog_json_schema`
        and :member:`pulsar_qrm.pulsar_qrm_qcodes._wave_json_schema`.

        Parameters
        ----------
        sequencer : int
            Sequencer index.
        file_name : str
            Sequencer waveforms and program file.

        Returns
        ----------

        Raises
        ----------
        Exception
            Invalid input parameter type.
        Exception
            An error is reported in system error and debug <= 1.
            All errors are read from system error and listed in the exception.
        Exception
            Assembly failed.
        SchemaError
            Invalid JSON file.
        """

        with open(file_name, 'r') as file:
            wave_and_prog_dict = json.load(file)
            validate(wave_and_prog_dict, self._wave_and_prog_json_schema)
            for name in wave_and_prog_dict["waveforms"]:
                validate(wave_and_prog_dict["waveforms"][name], self._wave_json_schema)
            for name in wave_and_prog_dict["weights"]:
                validate(wave_and_prog_dict["weights"][name], self._wave_json_schema)
            for name in wave_and_prog_dict["acquisitions"]:
                validate(wave_and_prog_dict["acquisitions"][name], self._acq_json_schema)
            self._delete_waveforms(sequencer)
            self._add_waveforms(sequencer, wave_and_prog_dict["waveforms"])
            self._delete_weights(sequencer)
            self._add_weights(sequencer, wave_and_prog_dict["weights"])
            self._delete_acquisitions(sequencer)
            self._add_acquisitions(sequencer, wave_and_prog_dict["acquisitions"])
            self._set_sequencer_program(sequencer, wave_and_prog_dict["program"])

    #--------------------------------------------------------------------------
    def __repr__(self) -> str:
        """
        Returns simplified representation of class giving just the class, name and connection.

        Parameters
        ----------

        Returns
        ----------
        str
            String representation of class.

        Raises
        ----------
        """

        loc_str = ""
        if hasattr(self._transport, '_socket'):
            address, port = self._transport._socket.getpeername()
            loc_str = f" at {address}:{port}"
        return f"<{type(self).__name__}: {self.name}" + loc_str + ">"

#-- class ---------------------------------------------------------------------

class pulsar_qrm(pulsar_qrm_qcodes):
    """
    Pulsar QRM driver class based on `QCoDeS <https://qcodes.github.io/Qcodes/>`_ that uses an IP socket to communicate
    with the instrument.
    """

    #--------------------------------------------------------------------------
    def __init__(self, name, host, port=5025, debug=0):
        """
        Creates Pulsar QRM driver object.

        Parameters
        ----------
        name : str
            Instrument name.
        host : str
            Instrument IP address.
        port : int
            Instrument port.
        debug : int
            Debug level (0 = normal, 1 = no version check, >1 = no version or error checking).

        Returns
        ----------

        Raises
        ----------
        Exception
            Debug level is 0 and there is a version mismatch.
        """

        #Create transport layer (socket interface)
        transport_inst = ip_transport(host=host, port=port)

        #Initialize parent classes.
        super(pulsar_qrm, self).__init__(name, transport_inst, debug)

#-- class ---------------------------------------------------------------------

class pulsar_qrm_dummy(pulsar_qrm_qcodes):
    """
    Pulsar QRM driver class based on `QCoDeS <https://qcodes.github.io/Qcodes/>`_ that uses the :class:`~ieee488_2.transport.pulsar_dummy_transport` layer
    to substitute an actual Pulsar QRM to allow software stack development without hardware.
    """

    #--------------------------------------------------------------------------
    def __init__(self, name, debug=1, is_rf_type=False):
        """
        Creates Pulsar QRM driver object. The debug level must be set to >= 1.

        Parameters
        ----------
        name : str
            Instrument name.
        debug : int
            Debug level (0 = normal, 1 = no version check, >1 = no version or error checking).
        is_rf_type : bool
            Dummy module type (False = RF, True = baseband)

        Returns
        ----------

        Raises
        ----------
        """

        #Create transport layer (socket interface)
        transport_inst = pulsar_dummy_transport(pulsar_qrm_ifc._get_acq_scope_config_format(), pulsar_qrm_ifc._get_sequencer_cfg_format(), is_rf_type)

        #Initialize parent classes.
        super(pulsar_qrm_dummy, self).__init__(name, transport_inst, debug)
