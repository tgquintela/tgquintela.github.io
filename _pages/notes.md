---
layout: archive
title: "Index of notes"
permalink: /notes/
author_profile: true
redirect_from:
  - /notes
---

{% include base_path %}

That is my personal collection of notes that I decided to make it public.
Most of the notes only have value as aggregators of bibliography material or ideas for projects.

In that index of notes it is showed the title and the last modification date of each note.


<ul>
{% for post in site.notes %}
    <li><a href="{{ base_path }}{{ post.url }}"><strong>{{ post.title }}</strong></a> {{ post.date.strftime('%Y-%m-%d') }}</li>
{% endfor %}
</ul>

* [**GDPR**](/notes/gdpr)    2018-04-10
* [**AWS**](/notes/aws)    2018-03-17
* [**Conflicts and wars statistics**](/notes/conflicts_and_wars_statistics)    2017-07-11
* **[Martingales](/notes/martingales)**    2016-06-01
* **[Stable distribution](/notes/stable_distribution)**    2016-06-01
* **[Operations Research](/notes/operations_research)**    2016-06-01
* **[Supply chain management](/notes/supply_chain_management)**    2016-06-01
* **[Search theory](/notes/search_theory)**    2016-06-01
* **[Machine Learning](/notes/machine_learning)**    2016-06-01
* **[Bagging](/notes/bagging)**    2016-06-01
* **[Random Forest](/notes/random_forest)**    2016-06-01
* **[Artificial Neural Networks](/notes/artificial_neural_networks)**    2016-06-01
* **[Sport and science list](/notes/sport_and_science_list)**    2016-06-01
* **[Tragedy of the anticommons](/notes/tragedy_of_the_anticommons)**    2016-06-01
* **[Game theory](/notes/game_theory)**    2016-06-01
* **[Dictator game](/notes/dictator_game)**    2016-06-01
* **[Nash equilibrium](/notes/nash_equilibrium)**    2016-06-01
* **[Somebody else's problem](/notes/somebody_else's_problem)**    2016-06-01
* **[Public goods game](/notes/public_goods_game)**    2016-06-01
* **[Chainstore paradox](/notes/chainstore_paradox)**    2016-06-01
* **[Tyranny of small decisions](/notes/tyranny_of_small_decisions)**    2016-06-01
* **[Blotto games](/notes/blotto_games)**    2016-06-01
* **[Non-cooperative game](/notes/non-cooperative_game)**    2016-06-01
* **[Alpha-beta pruning](/notes/alpha-beta_pruning)**    2016-06-01
* **[Ultimatum game](/notes/ultimatum_game)**    2016-06-01
* **[Social Choice Theory](/notes/social_choice_theory)**    2016-06-01
* **[Escalation of commitment](/notes/escalation_of_commitment)**    2016-06-01
* **[Trust game](/notes/trust_game)**    2016-06-01
* **[Zero-sum games](/notes/zero-sum_games)**    2016-06-01
* **[Stochastic game](/notes/stochastic_game)**    2016-06-01
* **[Algorithmic game theory](/notes/algorithmic_game_theory)**    2016-06-01
* **[Unscrupulous diner's dilemma](/notes/unscrupulous_diner's_dilemma)**    2016-06-01
* **[Traveler's dilemma](/notes/traveler's_dilemma)**    2016-06-01
* **[Tragedy of the commons](/notes/tragedy_of_the_commons)**    2016-06-01
* **[Arrow's impossibility theorem](/notes/arrow's_impossibility_theorem)**    2016-06-01
* **[Cooperative game](/notes/cooperative_game)**    2016-06-01
* **[Free rider problem](/notes/free_rider_problem)**    2016-06-01
* **[Prisoner's dilemma](/notes/prisoner's_dilemma)**    2016-06-01
* **[Parrondo's paradox](/notes/parrondo's_paradox)**    2016-06-01
* **[Bayesian game](/notes/bayesian_game)**    2016-06-01
* **[Sequential game](/notes/sequential_game)**    2016-06-01
* **[Counterfactual](/notes/counterfactual)**    2016-06-01
* **[Causality](/notes/causality)**    2016-06-01
* **[Causal network](/notes/causal_network)**    2016-06-01
* **[Granger causality](/notes/granger_causality)**    2016-06-01
* **[Confounding](/notes/confounding)**    2016-06-01
* **[Structural Equation Modeling](/notes/structural_equation_modeling)**    2016-06-01
* **[Causal diagram](/notes/causal_diagram)**    2016-06-01
* **[Julia](/notes/julia)**    2016-06-01
* **[Fortran](/notes/fortran)**    2016-06-01
* **[R](/notes/r)**    2016-06-01
* **[SAS](/notes/sas)**    2016-06-01
* **[Matlab](/notes/matlab)**    2016-06-01
* **[Java](/notes/java)**    2016-06-01
* **[Sage](/notes/sage)**    2016-06-01
* **[C](/notes/c)**    2016-06-01
* **[Go (Programming language)](/notes/go_(programming_language))**    2016-06-01
* **[Python](/notes/python)**    2016-06-01
* **[C. Elegans and Neuroscience](/notes/c._elegans_and_neuroscience)**    2016-06-01
* **[dMRI](/notes/dmri)**    2016-06-01
* **[Neuroscience](/notes/neuroscience)**    2016-06-01
* **[EEG](/notes/eeg)**    2016-06-01
* **[fMRI](/notes/fmri)**    2016-06-01
* **[Functional connectivity](/notes/functional_connectivity)**    2016-06-01
* **[Connectomics](/notes/connectomics)**    2016-06-01
* **[IPSP](/notes/ipsp)**    2016-06-01
* **[Action potentials](/notes/action_potentials)**    2016-06-01
* **[Broca-Wernicke model of language](/notes/broca-wernicke_model_of_language)**    2016-06-01
* **[Structural connectivity](/notes/structural_connectivity)**    2016-06-01
* **[Integrate-and-fire models](/notes/integrate-and-fire_models)**    2016-06-01
* **[EPSP](/notes/epsp)**    2016-06-01
* **[Hodgkin-Huxley model](/notes/hodgkin-huxley_model)**    2016-06-01
* **[PET](/notes/pet)**    2016-06-01
* **[Effective connectivity](/notes/effective_connectivity)**    2016-06-01
* **[Statistical physics](/notes/statistical_physics)**    2016-06-01
* **[Nonequilibrium Statistical Mechanics](/notes/nonequilibrium_statistical_mechanics)**    2016-06-01
* **[Tsallis entropy](/notes/tsallis_entropy)**    2016-06-01
* **[Fokker-Planck equation](/notes/fokker-planck_equation)**    2016-06-01
* **[Dissipative structures](/notes/dissipative_structures)**    2016-06-01
* **[Renormalization group](/notes/renormalization_group)**    2016-06-01
* **[Self-organization](/notes/self-organization)**    2016-06-01
* **[Caffe](/notes/caffe)**    2016-06-01
* **[Torch](/notes/torch)**    2016-06-01
* **[DeepDream](/notes/deepdream)**    2016-06-01
* **[Theano](/notes/theano)**    2016-06-01
* **[Lasagne](/notes/lasagne)**    2016-06-01
* **[TensorFlow](/notes/tensorflow)**    2016-06-01
* **[Hadoop](/notes/hadoop)**    2016-06-01
* **[Big Data](/notes/big_data)**    2016-06-01
* **[Pig](/notes/pig)**    2016-06-01
* **[Mahout](/notes/mahout)**    2016-06-01
* **[Hbase](/notes/hbase)**    2016-06-01
* **[Cloudera Impala](/notes/cloudera_impala)**    2016-06-01
* **[MapReduce](/notes/mapreduce)**    2016-06-01
* **[Spark](/notes/spark)**    2016-06-01
* **[Hive](/notes/hive)**    2016-06-01
* **[Theory of computation](/notes/theory_of_computation)**    2016-06-01
* **[Automata theory](/notes/automata_theory)**    2016-06-01
* **[Entscheidungsproblem](/notes/entscheidungsproblem)**    2016-06-01
* **[Computer complexity](/notes/computer_complexity)**    2016-06-01
* **[Context-free grammars](/notes/context-free_grammars)**    2016-06-01
* **[Chomsky hierarchy](/notes/chomsky_hierarchy)**    2016-06-01
* **[Game of life](/notes/game_of_life)**    2016-06-01
* **[Church-Turing thesis](/notes/church-turing_thesis)**    2016-06-01
* **[Algorithmics](/notes/algorithmics)**    2016-06-01
* **[Halting problem](/notes/halting_problem)**    2016-06-01
* **[P versus NP problem](/notes/p_versus_np_problem)**    2016-06-01
* **[Lambda calculus](/notes/lambda_calculus)**    2016-06-01
* **[Metaprogramming paradigm](/notes/metaprogramming_paradigm)**    2016-06-01
* **[Programming paradigm](/notes/programming_paradigm)**    2016-06-01
* **[Procedural programming](/notes/procedural_programming)**    2016-06-01
* **[Object-oriented programming](/notes/object-oriented_programming)**    2016-06-01
* **[Concurrent programming](/notes/concurrent_programming)**    2016-06-01
* **[Data-driven programming](/notes/data-driven_programming)**    2016-06-01
* **[Parallel programming](/notes/parallel_programming)**    2016-06-01
* **[Functional programming](/notes/functional_programming)**    2016-06-01
* **[Non-price competition](/notes/non-price_competition)**    2016-06-01
* **[Business models for open-source software](/notes/business_models_for_open-source_software)**    2016-06-01
* **[Market segmentation](/notes/market_segmentation)**    2016-06-01
* **[Business plan](/notes/business_plan)**    2016-06-01
* **[Market positioning](/notes/market_positioning)**    2016-06-01
* **[Niche market](/notes/niche_market)**    2016-06-01
* **[Neuromarketing](/notes/neuromarketing)**    2016-06-01
* **[Business Intelligence](/notes/business_intelligence)**    2016-06-01
* **[Location intelligence](/notes/location_intelligence)**    2016-06-01
* **[Target market](/notes/target_market)**    2016-06-01
* **[Marketing intelligence](/notes/marketing_intelligence)**    2016-06-01
* **[Business models](/notes/business_models)**    2016-06-01
* **[Artificial intelligence marketing](/notes/artificial_intelligence_marketing)**    2016-06-01
* **[Market penetration](/notes/market_penetration)**    2016-06-01
* **[Cross-selling](/notes/cross-selling)**    2016-06-01
* **[Upselling](/notes/upselling)**    2016-06-01
* **[Search Engine](/notes/search_engine)**    2016-06-01
* **[Latent Semantic Analysis](/notes/latent_semantic_analysis)**    2016-06-01
* **[Locality Sensitive Hashing](/notes/locality_sensitive_hashing)**    2016-06-01
* **[Latent Dirichlet Allocation](/notes/latent_dirichlet_allocation)**    2016-06-01
* **[Semantic Hashing](/notes/semantic_hashing)**    2016-06-01
* **[TF-IDF](/notes/tf-idf)**    2016-06-01
* **[Poisson process](/notes/poisson_process)**    2016-06-01
* **[Stochastic processes](/notes/stochastic_processes)**    2016-06-01
* **[Markov process](/notes/markov_process)**    2016-06-01
* **[Levy process](/notes/levy_process)**    2016-06-01
* **[Gamma process](/notes/gamma_process)**    2016-06-01
* **[Levy flight](/notes/levy_flight)**    2016-06-01
* **[Wiener process](/notes/wiener_process)**    2016-06-01
* **[AlphaGo](/notes/alphago)**    2016-06-01
* **[Natural language processing](/notes/natural_language_processing)**    2016-06-01
* **[AI-complete](/notes/ai-complete)**    2016-06-01
* **[Artificial Intelligence](/notes/artificial_intelligence)**    2016-06-01
* **[Computational intelligence](/notes/computational_intelligence)**    2016-06-01
* **[Computer vision](/notes/computer_vision)**    2016-06-01
* **[Waterfall software development](/notes/waterfall_software_development)**    2016-06-01
* **[Scrum](/notes/scrum)**    2016-06-01
* **[Software development process](/notes/software_development_process)**    2016-06-01
* **[Agile software development](/notes/agile_software_development)**    2016-06-01
* **[Pair programming](/notes/pair_programming)**    2016-06-01
* **[Extreme programming](/notes/extreme_programming)**    2016-06-01
* **[Race to the bottom](/notes/race_to_the_bottom)**    2016-06-01
* **[Streisand effect](/notes/streisand_effect)**    2016-06-01
* **[Milgram experiment](/notes/milgram_experiment)**    2016-06-01
* **[Social trap](/notes/social_trap)**    2016-06-01
* **[Cross-validation](/notes/cross-validation)**    2016-06-01
* **[Sampling](/notes/sampling)**    2016-06-01
* **[AB testing](/notes/ab_testing)**    2016-06-01
* **[Bootstrapping](/notes/bootstrapping)**    2016-06-01
* **[Statistic Type errors](/notes/statistic_type_errors)**    2016-06-01
* **[Statistical testing](/notes/statistical_testing)**    2016-06-01
* **[Jackknife](/notes/jackknife)**    2016-06-01
* **[Parametric and nonparametric statistics](/notes/parametric_and_nonparametric_statistics)**    2016-06-01
* **[Permutation tests](/notes/permutation_tests)**    2016-06-01
* **[Resampling methods](/notes/resampling_methods)**    2016-06-01
* **[Normed space](/notes/normed_space)**    2016-06-01
* **[Hilbert space](/notes/hilbert_space)**    2016-06-01
* **[Normal space](/notes/normal_space)**    2016-06-01
* **[Inner-product space](/notes/inner-product_space)**    2016-06-01
* **[Banach space](/notes/banach_space)**    2016-06-01
* **[Functional analysis](/notes/functional_analysis)**    2016-06-01
* **[Topological space](/notes/topological_space)**    2016-06-01
* **[Complete metric space](/notes/complete_metric_space)**    2016-06-01
* **[Hausdorff space](/notes/hausdorff_space)**    2016-06-01
* **[Metric space](/notes/metric_space)**    2016-06-01
* **[Macroecology](/notes/macroecology)**    2016-06-01
* **[Mutualistic networks](/notes/mutualistic_networks)**    2016-06-01
* **[Abundance](/notes/abundance)**    2016-06-01
* **[Ecology](/notes/ecology)**    2016-06-01
* **[Niche modelling](/notes/niche_modelling)**    2016-06-01
* **[Coevolution](/notes/coevolution)**    2016-06-01
* **[Ecosystems](/notes/ecosystems)**    2016-06-01
* **[Spatial ecology](/notes/spatial_ecology)**    2016-06-01
* **[Trolley problem](/notes/trolley_problem)**    2016-06-01
* **[Linear programming](/notes/linear_programming)**    2016-06-01
* **[Nonlinear programming](/notes/nonlinear_programming)**    2016-06-01
* **[Convex optimization](/notes/convex_optimization)**    2016-06-01
* **[Dynamic programming](/notes/dynamic_programming)**    2016-06-01
* **[Mathematical optimization](/notes/mathematical_optimization)**    2016-06-01
* **[Stochastic optimization](/notes/stochastic_optimization)**    2016-06-01
* **[Combinatorial optimization](/notes/combinatorial_optimization)**    2016-06-01
* **[Multi-objective optimization](/notes/multi-objective_optimization)**    2016-06-01
* **[Integer programming](/notes/integer_programming)**    2016-06-01
* **[Linear-fractional programming](/notes/linear-fractional_programming)**    2016-06-01
* **[Fiscal dumping](/notes/fiscal_dumping)**    2016-06-01
* **[High-frequency trade](/notes/high-frequency_trade)**    2016-06-01
* **[Homo economicus](/notes/homo_economicus)**    2016-06-01
* **[Aggregation problem](/notes/aggregation_problem)**    2016-06-01
* **[Behavioral economics](/notes/behavioral_economics)**    2016-06-01
* **[Social dumping](/notes/social_dumping)**    2016-06-01
* **[Economic freedom](/notes/economic_freedom)**    2016-06-01
* **[Shallow banking](/notes/shallow_banking)**    2016-06-01
* **[Malthusian trap](/notes/malthusian_trap)**    2016-06-01
* **[Efficient market hypothesis](/notes/efficient_market_hypothesis)**    2016-06-01
* **[Paradox of competetion](/notes/paradox_of_competetion)**    2016-06-01
* **[Bubble theory](/notes/bubble_theory)**    2016-06-01
* **[Economies of scale](/notes/economies_of_scale)**    2016-06-01
* **[Price dumping](/notes/price_dumping)**    2016-06-01
* **[Black-Scholes model](/notes/black-scholes_model)**    2016-06-01
* **[Digital economy](/notes/digital_economy)**    2016-06-01
* **[Evolutionary Economics](/notes/evolutionary_economics)**    2016-06-01
* **[Risk-return tradeoff](/notes/risk-return_tradeoff)**    2016-06-01
* **[Economic Liberalism](/notes/economic_liberalism)**    2016-06-01
* **[Neuroeconomics](/notes/neuroeconomics)**    2016-06-01
* **[Capitalism](/notes/capitalism)**    2016-06-01
* **[Ergodic Theory](/notes/ergodic_theory)**    2016-06-01
* **[Lyapunov exponent](/notes/lyapunov_exponent)**    2016-06-01
* **[Feigenbaum constant](/notes/feigenbaum_constant)**    2016-06-01
* **[Haussdorff dimension](/notes/haussdorff_dimension)**    2016-06-01
* **[Smale's horseshoe map](/notes/smale's_horseshoe_map)**    2016-06-01
* **[Poincaré-Bendixson theorem](/notes/poincaré-bendixson_theorem)**    2016-06-01
* **[Git](/notes/git)**    2016-06-01
* **[Vi_Vim](/notes/vi_vim)**    2016-06-01
* **[emacs](/notes/emacs)**    2016-06-01
* **[Docker](/notes/docker)**    2016-06-01
* **[Markdown](/notes/markdown)**    2016-06-01
* **[reStructuredText](/notes/restructuredtext)**    2016-06-01
* **[Data extraction](/notes/data_extraction)**    2016-06-01
* **[Data management](/notes/data_management)**    2016-06-01
* **[Data Analysis](/notes/data_analysis)**    2016-06-01
* **[Exploratory Data Analysis](/notes/exploratory_data_analysis)**    2016-06-01
* **[Scikitlearn](/notes/scikitlearn)**    2016-06-01
* **[Data munging](/notes/data_munging)**    2016-06-01
* **[Data visualization](/notes/data_visualization)**    2016-06-01
* **[Unbalance data problem](/notes/unbalance_data_problem)**    2016-06-01
* **[Feature Selection](/notes/feature_selection)**    2016-06-01
* **[Measures to evaluate and decide in ML](/notes/measures_to_evaluate_and_decide_in_ml)**    2016-06-01
* **[Spatial Data Analysis](/notes/spatial_data_analysis)**    2016-06-01
* **[Brexit](/notes/brexit)**    2016-06-01
* **[Art and maths](/notes/art_and_maths)**    2016-06-01


<script type="text/javascript">
  var GOOG_FIXURL_LANG = 'en',
      GOOG_FIXURL_SITE = '{{ site.url }}'.concat('/notes/');
//          GOOG_FIXURL_SITE = 'https://tgquintela.github.io/notes/';
//      domain = '{{ site.url }}',
//      domain = domain.concat('/notes/');
</script>
<script type="text/javascript"
  src="//linkhelp.clients.google.com/tbproxy/lh/wm/fixurl.js">
</script>

