#include "XyloLayer.h"
#include <iostream>

/**
 * Constructor of the layer. Needs all connectivity and neuron parameters.
 * The number of neurons is inferred by the length of dash_syns.
 * The number if outputs in inferred by the length of dash_syns_out.
 *
 */
XyloLayer::XyloLayer(const std::vector<std::vector<struct XyloSynapse*>>& synapses_in,
                         const std::vector<std::vector<struct XyloSynapse*>>& synapses_rec,
                         const std::vector<std::vector<struct XyloSynapse*>>& synapses_out,
                         const std::vector<std::vector<uint16_t>>& aliases,
                         const std::vector<int16_t> v_th,
                         const std::vector<int16_t> v_th_out,
                         const int8_t weight_shift_inp,
                         const int8_t weight_shift_rec,
                         const int8_t weight_shift_out,
                         const std::vector<uint8_t>& dash_mem,
                         const std::vector<uint8_t>& dash_mem_out,
                         const std::vector<std::vector<uint8_t>>& dash_syns,
                         const std::vector<std::vector<uint8_t>>& dash_syns_out,
                         const std::string &name) : synapses_in(synapses_in),
                                                    synapses_rec(synapses_rec),
                                                    synapses_out(synapses_out),
                                                    aliases(aliases),
                                                    weight_shift_inp(weight_shift_inp),
                                                    weight_shift_rec(weight_shift_rec),
                                                    weight_shift_out(weight_shift_out),
                                                    name(name)
{ 
    auto it_v_th = v_th.begin();
    auto it_dash_mem = dash_mem.begin();
    auto it_dash_syn = dash_syns.begin();
    while(it_dash_syn != dash_syns.end())
    {
        iaf_neurons.push_back(new XyloIAFNeuron(*it_dash_mem++, 
                                                  *it_dash_syn++, 
                                                  *it_v_th++));
        rec_i_syn.push_back(new std::vector<int16_t>());
        rec_i_syn2.push_back(new std::vector<int16_t>());
        rec_v_mem.push_back(new std::vector<int16_t>());

        // init spike buffer
        recurrent_spikes.push_back(0);
    }

    auto it_v_th_out = v_th_out.begin();
    auto it_dash_mem_out = dash_mem_out.begin();
    auto it_dash_syn_out = dash_syns_out.begin();
    while(it_dash_syn_out != dash_syns_out.end())
    {
        iaf_neurons_out.push_back(new XyloIAFNeuron(*it_dash_mem_out++, 
                                                      *it_dash_syn_out++,
                                                      *it_v_th_out++));
        rec_i_syn_out.push_back(new std::vector<int16_t>());
        rec_i_syn2_out.push_back(new std::vector<int16_t>());
        rec_v_mem_out.push_back(new std::vector<int16_t>());

        // init spike buffer
        out_spikes.push_back(0);
    }

}

/**
 * Resets all neurons and clears recordings.
 */
void XyloLayer::reset_all()
{
    for (auto it_neuron = iaf_neurons.begin(); 
         it_neuron != iaf_neurons.end(); 
         ++it_neuron)
    {
        XyloIAFNeuron* n = *it_neuron; 
        n->reset();
    }

    for (auto it_neuron_out = iaf_neurons_out.begin(); 
         it_neuron_out != iaf_neurons_out.end(); 
         ++it_neuron_out)
    {
        XyloIAFNeuron* n = *it_neuron_out; 
        n->reset();
    }

    clear_recordings();

    for(int i=0; i<recurrent_spikes.size();i++){
        recurrent_spikes[i] = 0;
    }  

    for(int i=0; i<out_spikes.size();i++){
        recurrent_spikes[i] = 0;
    } 

}

/**
 * Clears all recordings.
 */ 
void XyloLayer::clear_recordings()
{
    // clear recordings
    for (auto it_rec = rec_i_syn.begin();
         it_rec != rec_i_syn.end(); 
         ++it_rec)
    {
        std::vector<int16_t>* tmp = *it_rec;
        tmp->clear();
    }

    for (auto it_rec = rec_i_syn2.begin();
         it_rec != rec_i_syn2.end(); 
         ++it_rec)
    {
        std::vector<int16_t>* tmp = *it_rec;
        tmp->clear();
    }

    for (auto it_rec = rec_v_mem.begin(); 
         it_rec != rec_v_mem.end(); 
         ++it_rec)
    {
        std::vector<int16_t>* tmp = *it_rec;
        tmp->clear();
    }

    for (auto it_rec = rec_i_syn_out.begin(); 
         it_rec != rec_i_syn_out.end();
         ++it_rec)
    {
        std::vector<int16_t>* tmp = *it_rec;
        tmp->clear();
    }

    for (auto it_rec = rec_i_syn2_out.begin(); 
         it_rec != rec_i_syn2_out.end();
         ++it_rec)
    {
        std::vector<int16_t>* tmp = *it_rec;
        tmp->clear();
    }

    for (auto it_rec = rec_v_mem_out.begin();
         it_rec != rec_v_mem_out.end(); 
         ++it_rec)
    {
        std::vector<int16_t>* tmp = *it_rec;
        tmp->clear();
    }

    rec_recurrent_spikes.clear();
    rec_out_spikes.clear();
}

/**
 * Evolves the complete network.\n
 * Takes a 2D vector as input with the shape (time, num_input_neurons) containing the number of input spikes. \n
 * Iterates over input time and executes the folling operation in this order: \n
 *      Deliver all input spikes of current timestep to their target neurons.\n
 *      Deliver all recurrent spikes from last timestep to their target neurons including output neurons. \n
 *      Evolve all neurons and storing their spikes for delivery in the next timestep.\n
 *      Evolve all output neurons and storing their spikes in the output buffer. \n
 *
 *  All membrane potentials, synaptic currents and spikes are recorded.
 *  
 *  Returns the output spikes.      
 * 
 */
std::vector<std::vector<uint8_t>> XyloLayer::evolve(std::vector<std::vector<uint8_t>> input)
{
    clear_recordings();

    // iterate over input
    for (auto it_time = input.begin(); it_time != input.end(); ++it_time)
    {
        uint16_t time__ = std::distance(input.begin(), it_time);

        // deliver input spikes
        std::vector<uint8_t> inp_spikes = *it_time;
        for (auto it_inp = inp_spikes.begin(); it_inp != inp_spikes.end(); ++it_inp)
        {
            uint8_t num_spikes = *it_inp;

            // limit number of input spikes to MAX_NUM_INP_SPIKES
            if (num_spikes > MAX_NUM_INP_SPIKES)
            {
                num_spikes = MAX_NUM_INP_SPIKES;
            }

            if (num_spikes > 0)
            {
                uint16_t inp_pre = std::distance(inp_spikes.begin(), it_inp);
                std::vector<XyloSynapse*> post_synapses_in = synapses_in.at(inp_pre);
                
                // iterate over postsynaptic neurons
                for (auto it_synapse = post_synapses_in.begin(); 
                     it_synapse != post_synapses_in.end(); 
                     ++it_synapse)
                {
                    XyloSynapse* w = *it_synapse;
                    XyloIAFNeuron* post_neuron = iaf_neurons[w->target_neuron_id];
                    for (int i = 0; i < num_spikes; ++i)
                        post_neuron->receiveSpike(w->weight << weight_shift_inp, w->target_synapse_id);
                }
            }
        }

        // deliver recurrent spikes
        for (auto it_rec = recurrent_spikes.begin(); 
             it_rec != recurrent_spikes.end(); 
             ++it_rec)
        {
            uint8_t num_spikes = *it_rec;

            if (num_spikes > 0)
            {
                uint16_t rec_pre = std::distance(recurrent_spikes.begin(), it_rec);

                // iterate over postsynaptic neurons
                std::vector<XyloSynapse*> post_synapses_rec = synapses_rec.at(rec_pre);
                for (auto it_synapse = post_synapses_rec.begin(); 
                     it_synapse != post_synapses_rec.end(); 
                     ++it_synapse)
                {
                    XyloSynapse* w = *it_synapse;
                    XyloIAFNeuron* post_neuron = iaf_neurons[w->target_neuron_id];
                    for (int i = 0; i < num_spikes; ++i)
                        post_neuron->receiveSpike(w->weight << weight_shift_rec, w->target_synapse_id);
                }

                // iterate over postsynaptic readout neurons
                std::vector<XyloSynapse*> post_synapses_out = synapses_out.at(rec_pre);
                for (auto it_synapse = post_synapses_out.begin(); 
                     it_synapse != post_synapses_out.end(); 
                     ++it_synapse)
                {
                    XyloSynapse* w = *it_synapse;
                    XyloIAFNeuron* post_neuron = iaf_neurons_out[w->target_neuron_id];
                    for (int i = 0; i < num_spikes; ++i)
                        post_neuron->receiveSpike(w->weight << weight_shift_out, w->target_synapse_id);
                }
            }
            // clear spike buffer
            *it_rec = 0;
        }
        
        // evolve neurons
        for (auto it_nid = iaf_neurons.begin(); 
             it_nid != iaf_neurons.end(); 
             ++it_nid)
        {
            XyloIAFNeuron* neuron = *it_nid; 
            uint16_t nid = std::distance(iaf_neurons.begin(), it_nid);

            // check if this neuron has already some spikes as alias
            uint8_t num_spikes = recurrent_spikes.at(nid);

            neuron->decayState();
            num_spikes = neuron->evolve(num_spikes, MAX_NUM_SPIKES);

            recurrent_spikes.at(nid) = num_spikes; 

            // make aliases spike
            std::vector<uint16_t> alias = aliases.at(nid);
            for (auto it_alias = alias.begin(); it_alias != alias.end(); ++it_alias)
            {
                uint16_t alias_nid = *it_alias;
                // make sure the alias does not spike too often
                uint8_t spikes_to_add = recurrent_spikes.at(nid);
                if (recurrent_spikes.at(alias_nid) + spikes_to_add > MAX_NUM_SPIKES)
                {
                    recurrent_spikes.at(alias_nid) = MAX_NUM_SPIKES;
                }
                else
                {
                    recurrent_spikes.at(alias_nid) += spikes_to_add;
                }
            }

            // TODO record all synaptic states
            rec_i_syn.at(nid)->push_back(neuron->i_syns.at(0));
            if (neuron->i_syns.size() > 1)
            {
                rec_i_syn2.at(nid)->push_back(neuron->i_syns.at(1));
            }           
            rec_v_mem.at(nid)->push_back(neuron->v_mem);
        }

        // evolve readout neurons
        for (auto it_nid = iaf_neurons_out.begin(); 
             it_nid != iaf_neurons_out.end(); 
             ++it_nid)
        {
            XyloIAFNeuron* neuron = *it_nid; 
            uint16_t nid = std::distance(iaf_neurons_out.begin(), it_nid);

            neuron->decayState();
            uint8_t num_spikes = neuron->evolve(0, MAX_NUM_OUT_SPIKES);

            out_spikes.at(nid) = num_spikes; 

            // TODO record all synaptic states
            rec_i_syn_out.at(nid)->push_back(neuron->i_syns.at(0));
            if (neuron->i_syns.size() > 1)
            {
                rec_i_syn2_out.at(nid)->push_back(neuron->i_syns.at(1));
            }
            rec_v_mem_out.at(nid)->push_back(neuron->v_mem);
        }

        rec_recurrent_spikes.push_back(std::vector<uint8_t>(recurrent_spikes));
        rec_out_spikes.push_back(std::vector<uint8_t>(out_spikes));

    }

    return rec_out_spikes;
}



