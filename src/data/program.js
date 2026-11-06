// GAMA Days 2026 — tentative conference program.
// Set `timezone` (e.g. "CET (UTC+1)") to display it on the program page.
export const timezone = "Paris time (CET, UTC+1)";

const s = (time, speaker, title) => ({ time, speaker, title });

export const days = [
  {
    id: "nov-23",
    label: "Monday 23 November",
    short: "23 Nov",
    blocks: [
      { type: "event", time: "10:00 – 10:15", title: "Conference opening" },
      {
        type: "session", code: "1a", name: "GAMA: Technological Integration, Tool Development and Model Analysis",
        talks: [
          s("10:15 – 10:30", "Huynh Quang Nghi", "Next-Generation Infrastructure for GAMA: IDE Extensions, Containerization, and Mobile Integration"),
          s("10:30 – 10:45", "Ngongang Ruben Petteng", "Exporting standalone GAMA simulation, from an IDE project to a simplified executable usage"),
          s("10:45 – 11:00", "Dang Thai Son", "Moov'Hanoi: Design of a web-based architecture for operationalizing GAMA mobility simulations"),
          s("11:00 – 11:15", "Barbe Florian", "Project SIMPLE: Simplifying the integration of GAMA with Unity 3D"),
        ],
      },
      {
        type: "session", code: "2a", name: "Environmental and Ecological Modeling",
        talks: [
          s("11:15 – 11:30", "Cabatingan Joanne Maryz", "An agent-based model of insecticide resistance in the brown planthopper: Comparing spray strategies in Mekong Delta rice"),
          s("11:30 – 11:45", "Arnejo Zenith", "Exploring Future Giant-Clam Trade and Conservation Trajectories Using a CITES-Informed Agent-Based Model"),
          s("11:45 – 12:00", "Chaiprom Usawadee", "BiodiVRestorer VU2: A GAMA-Driven Virtual Reality for Biodiversity Restoration, Toward School Curriculum Integration"),
          s("12:00 – 12:15", "Delattre Hadrien", "BioChains; a model for bioprocesses, biomass fluxes and logistics to simulate bioeconomy scenarii"),
          s("12:15 – 12:30", "Proverbio Daniele", "Proof-of-concept BDI modeling of green corridors for wildlife protection"),
        ],
      },
      { type: "break", title: "Lunch break" },
      { type: "keynote", time: "14:00 – 14:30", speaker: "Peer-Olaf Siebers", title: "A Software Engineer's Approach to Co-Creating Agent-Based Models" },
      {
        type: "session", code: "3a", name: "Algorithms, Artificial Intelligence and Intelligent Agent Modeling",
        talks: [
          s("14:30 – 14:45", "Paul Saves", "MIMIcking the COmplexity of agent-based models: the MIMICO Project"),
          s("14:45 – 15:00", "Kong Haojia", "Coupling GAMA with LLMs for Simulating Dialogues Among Agents: An Application to Farmers' Attitudes Toward Smart Water Meters"),
          s("15:00 – 15:15", "Carvajal Bastidas Hernan David", "A reusable Gale-Shapley matching module for GAMA"),
          s("15:15 – 15:30", "Ariel Noyman", "What if Networks Could Reason? Agent Guidance by Decision Models at Spatial Nodes"),
        ],
      },
      {
        type: "session", code: "2b", name: "Environmental and Ecological Modeling",
        talks: [
          s("15:30 – 15:45", "Boton Xavier", "A livestock feed ration optimization model for agri-food scenarios"),
          s("15:45 – 16:00", "Le Goff Morgane", "A model to quantify the effect of diversity within the herd on the resilience of dairy sheep farming systems in the face of climate change"),
          s("16:00 – 16:15", "Sok Chanattan", "Quantifying Building-Related Climate Impacts in Hamburg through a Digital Twin"),
          s("16:15 – 16:30", "Szurlej Mikołaj", "Simulating Habit Formation in Urban Green Infrastructures: A Spatial Anchor Mechanism in the Strolling Activity Simulator (SAS)"),
          s("16:30 – 16:45", "Taillandier Patrick", "STARFARM: An Agent-Based Model for Exploring Agroecological Transitions in the Vietnamese Mekong Delta"),
        ],
      },
    ],
  },
  {
    id: "nov-24",
    label: "Tuesday 24 November",
    short: "24 Nov",
    blocks: [
      { type: "keynote", time: "10:00 – 10:30", speaker: "GAMA Team", title: "General news on GAMA" },
      {
        type: "session", code: "1b", name: "GAMA: Technological Integration, Tool Development and Model Analysis",
        talks: [
          s("10:30 – 10:45", "Lesquoy Baptiste", "A server-client architecture for model coupling: the case of MAELIA and STICS"),
          s("10:45 – 11:00", "Grosjean Lucas", "Distributing GAMA Simulations on HPC Clusters with the Distribution Model"),
          s("11:00 – 11:15", "Lesquoy Baptiste", "Sensitivity Analysis in Hierarchical and Mixed Parameter Space. Application to Decision Rules of the MAELIA model"),
          s("11:15 – 11:30", "Brugière Arthur", "TANGO: An open-source framework to visualize GAMA simulations through tangible robots"),
        ],
      },
      {
        type: "session", code: "4a", name: "Health, Education and Disaster Risk Simulation",
        talks: [
          s("11:30 – 11:45", "Huong Ngan Vu", "Comparative Analysis of Evacuation Scenarios using Agent-based Modelling: The 2020 Flood Event in Vietnam"),
          s("11:45 – 12:00", "Nguyen Thanh Do", "FastBathtub - a fast, interactive, reduced-complexity flood-inundation agent-based model implemented in GAMA"),
          s("12:00 – 12:15", "Seth Rattanak", "Modelling insect interactions in rice crops on the GAMA platform as a basis for educational VR games"),
          s("12:15 – 12:30", "Chapuis Kevin", "From Simulation to Situated Experience: Coupling GAMA and Unity for Immersive Tsunami Risk Awareness in Mayotte"),
          s("12:30 – 12:45", "Dmochowski Tymon", "From Urban Design to Population Health: Agent-Based Modelling as a Translational Medicine Tool"),
        ],
      },
      { type: "break", title: "Lunch break" },
      {
        type: "session", code: "5a", name: "Urban Planning and Mobility Simulation",
        talks: [
          s("14:00 – 14:15", "Quintana-Rodriguez Francisco", "Agent-Based Simulation of Insecurity Perception and Pedestrian Route Choice in Student Mobility in Central Guadalajara"),
          s("14:15 – 14:30", "Contreras Jaime", "Amenities, Quality of Life, and Displacement: A Cellular Automaton and Agent-Based Model of Gentrification"),
          s("14:30 – 14:45", "Lomelin Juan Pablo", "An Agent-Based Model of Neighbourhood Security, Housing Prices and Displacement in GAMA"),
          s("14:45 – 15:00", "Palomo-Briones Gamaliel", "An Integrated GAMA Framework for Urban Mobility: From Mode Choice Decisions to Network Congestion Dynamics"),
          s("15:00 – 15:15", "Wang Zening", "Evaluating Green Streetscape Interventions with GAMA: Pedestrian, Vehicle, and Ecological Trade-offs in Gowanus"),
          s("15:15 – 15:30", "Castillo Kenneth", "Urban Mobility Improvement Methods and Their Acceptance: An Agent-Based Model of Commuter Mode Choice"),
          s("15:30 – 15:45", "Pierre Georine", "A Pedestrian Mobility Simulation Tool for Evaluating Transit Expansion and Densification in Freetown, Sierra Leone"),
        ],
      },
      {
        type: "session", code: "3b", name: "Algorithms, Artificial Intelligence and Intelligent Agent Modeling",
        talks: [
          s("15:45 – 16:00", "Soulé Julien", "GAMAX: Compiling GAML Models to JAX for Faster Simulations"),
          s("16:00 – 16:15", "Lesquoy Baptiste", "Learning in and with GAMA: bridging agent-based modelling and machine learning"),
          s("16:15 – 16:30", "Gaudou Benoit", "Plugging Language Models into GAMA Mobility Simulations: Generative Mode Choice Against a Real Household Travel Survey"),
          s("16:30 – 16:45", "Kakeu Tuekam Severin Vianey", "SBDI Architecture: Enabling Spatial Reasoning in Cognitive Agents for Traffic Simulations"),
        ],
      },
    ],
  },
  {
    id: "nov-25",
    label: "Wednesday 25 November",
    short: "25 Nov",
    blocks: [
      {
        type: "session", code: "6a", name: "Participatory, Policy and Social Modeling",
        talks: [
          s("10:00 – 10:15", "Seghouani Mounir", "Using MAELIA platform for participatory climate adaptation of agricultural territories: an integrated assessment and multiagent modelling approach"),
          s("10:15 – 10:30", "Tenma Ryota", "Development of a Participatory Urban Design Environment Based on Stylized Representations of Urban Structure"),
          s("10:30 – 10:45", "Robert Czajka", "From Relief Camp to Slum or City: in silico testing of how socio-spatial moderators steer migrant co-adaptation between criminalisation and self-revitalisation"),
          s("10:45 – 11:00", "Biré Léo", "Of interactive simulations and bureaucrats – participatory research navigating hydraulic uncertainties"),
          s("11:00 – 11:15", "Gaza John Cedric", "An agent-based model of public Junior High School choice: A case study in San Pablo City, Philippines"),
        ],
      },
      {
        type: "session", code: "5b", name: "Urban Planning and Mobility Simulation",
        talks: [
          s("11:15 – 11:30", "Kimbangi Menakuntima Rabbi", "Agent-based modelling of traffic jam emergence at an urban roundabout in Kinshasa"),
          s("11:30 – 11:45", "Cueille Elisa", "Activity-Based Model in GAMA: Application to Hanoi's Mobility Transition"),
          s("11:45 – 12:00", "Vaulot Pierre", "Simulating Commuter Mobility in the Gipuzkoa Region: An Agent-Based Approach using GAMA"),
          s("12:00 – 12:15", "Biegel Jelle", "Using Agent-Based modelling to design urban food environments surrounding schools for adolescents. A case study on Strandeiland, Amsterdam"),
        ],
      },
      { type: "break", title: "Lunch break" },
      {
        type: "session", code: "6b", name: "Participatory, Policy and Social Modeling",
        talks: [
          s("14:00 – 14:15", "Stolte Gregor", "Simulating Online Debates"),
          s("14:15 – 14:30", "Tokarska-Gołębiewska Ewa", "Prognostic CPTED: in silico testing of how neighborhood form steers adolescent socialization between cooperation and criminalization"),
          s("14:30 – 14:45", "Szymon Dziedzic", "From Iterated Prisoner's Dilemma to Design Standards: Which Laws of Cooperation Hold When Combined?"),
          s("14:45 – 15:00", "Georgiou Luce", "A Participatory Simulation Tool in Virtual Reality for Managing Stormwater Nature-Based Solutions"),
          s("15:00 – 15:15", "Gomez Gonzalez Elliot", "Hoarding or Solidarity? An Agent-Based Simulation for the Self-Regulation of Shared Water Resources"),
        ],
      },
      {
        type: "session", code: "4b", name: "Health, Education and Disaster Risk Simulation",
        talks: [
          s("15:15 – 15:30", "Chapuis Kevin", "TsunaWAVE: coupling uncertain landslide-generated tsunami scenarios with agent-based evacuation modelling through an interactive web platform. Application to Mamoudzou (Mayotte, France)"),
          s("15:30 – 15:45", "Renard Mathieu", "Hybridization of conceptual modeling and agent-based simulation in a context of climate change-related crisis management"),
          s("15:45 – 16:00", "Szarejko Maciej", "Psychoergonomics as Environmental Behavioural Medicine: A Translational Path Built on In Silico Experiments in GAMA for Adolescent Digital Addiction Prevention"),
          s("16:00 – 16:15", "Sabaj Jagoda", "Simulating Autistic Spatial Related Experience in Public Offices: A Psychoergonomic in Silico Experiments in GAMA Platform"),
          s("16:15 – 16:30", "Pia Figueroa Samuel", "Agent-Based Modeling of Urban Flooding and Storm Drainage Performance Under Rainfall and Waste Conditions"),
        ],
      },
      { type: "event", time: "16:30 – 16:45", title: "Conference closing" },
    ],
  },
];
