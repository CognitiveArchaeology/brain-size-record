# -*- coding: utf-8 -*-
"""
Verified bibliographic record for every paper cited in the hub.

Every field here was read off the publisher's own page or PDF during the
2026-08-15 verification pass. Nothing in this file is from recall.
Where a publisher states conflicting values (Karger gives three different
publication dates for BBE 98(2)), the conflict is recorded rather than resolved.
"""

PAPERS = {
    # ---------------------------------------------------------------- core five
    "desilva2023": {
        "key": "desilva2023",
        "slug": "desilva-2023-brains-have-shrunk",
        "title": "Human brains have shrunk: the questions are when and why",
        "authors": ["Jeremy M. DeSilva", "Luke D. Fannin", "Isabelle Cheney",
                    "Alexander G. Claxton", "Iulian Ilieş", "Jessica Kittelberger",
                    "Jeff Morgan Stibel", "James F. A. Traniello"],
        "author_short": "DeSilva et al.",
        "journal": "Frontiers in Ecology and Evolution",
        "volume": "11", "pages": "1191274", "year": 2023,
        "doi": "10.3389/fevo.2023.1191274",
        "url": "https://www.frontiersin.org/journals/ecology-and-evolution/articles/10.3389/fevo.2023.1191274/full",
        "license": "CC BY 4.0", "license_url": "https://creativecommons.org/licenses/by/4.0/",
        "oa": "Gold open access",
        "dates": "Received 21 Mar 2023; accepted 29 May 2023; published 22 Jun 2023",
        "type": "Perspective",
        "role": "Round 3 of the Holocene brain size exchange — the authors' response to Villmoare & Grabowski (2022).",
        "abstract": (
            "Human brain reduction from the Late Pleistocene/Holocene to the modern day is a "
            "longstanding anthropological observation documented with numerous lines of independent "
            "evidence. In a recent study (DeSilva et al., 2021), we analyzed a large compilation of "
            "fossil and recent human crania and determined that this reduction was surprisingly "
            "recent, occurring rapidly within the past 5,000 to 3,000 years of human history. We "
            "attributed such a change as a consequence of population growth and cooperative "
            "intelligence and drew parallels with similar evolutionary trends in eusocial insects, "
            "such as ants. In a reply to our study, Villmoare and Grabowski (2022) reassessed our "
            "findings using portions of our dataset and were unable to detect any reduction in brain "
            "volume during this time frame. In this paper, responding to Villmoare and Grabowski's "
            "critique, we reaffirm recent human brain size reduction in the Holocene, and encourage "
            "our colleagues to continue to investigate both the timing and causes of brain size "
            "reduction in humans in the past 10,000 years."),
        "findings": [
            "Across 19 published studies over roughly 90 years, the average reported decrease in human brain size from the Late Pleistocene/Holocene to today is <strong>8.5%</strong>.",
            "Pleistocene <em>H. sapiens</em> brains average <strong>1,458 ± 140 cc</strong> (n = 136) — effectively identical to Würm-period Neanderthals at 1,459 ± 182 cc (n = 14).",
            "The Pleistocene–Holocene difference in cranial capacity is statistically significant (Welch's <em>t</em> = 9.15, <em>p</em> &lt; 0.0001), as is the decrease after 3 ka (<em>t</em> = 12.81, <em>p</em> &lt; 0.0001).",
            "Estimated reduction after 3,000 years: <strong>159 cc</strong> using the authors' modern estimate, or <strong>117 cc</strong> using Beals et al. (1984) — described in text as a 100–150 cc reduction.",
            "The result holds across three independent modern reference datasets (Dekaban &amp; Sadowsky n = 3,399, <em>t</em> = 9.83; Beals et al. n = 5,288, <em>t</em> = 9.04; both <em>p</em> &lt; 0.0001).",
            "Framed as effect size: human brain volume has decreased by roughly <strong>one standard deviation</strong> in the last 10,000 years, whether examined locally or globally.",
        ],
        "limitations": [
            "The authors concede the Holocene portion of the original dataset is skewed toward modern specimens — an unavoidable taphonomic bias that may pull the change-point estimate too recent and could obscure earlier change points.",
            "They acknowledge the historical brain-size literature is &ldquo;rife with problematic studies biased by racist and sexist objectives,&rdquo; and that measurement methods differ across investigators.",
            "The Morton Collection data were removed from this analysis; the authors note it &ldquo;has been used to promote false and dangerous ideas of white supremacy.&rdquo; Removing it had no appreciable effect on the modern estimate.",
            "Errata are disclosed: four juvenile Neanderthals and one duplicate entry were removed from the original dataset, and an uncited prior work (Henneberg 2004) is credited.",
            "The authors state brain reduction probably occurred at different rates in different regions, and call for more Holocene samples.",
        ],
    },

    "stibel2023climate": {
        "key": "stibel2023climate",
        "slug": "stibel-2023-climate-brain-size",
        "title": "Climate Change Influences Brain Size in Humans",
        "authors": ["Jeff Morgan Stibel"],
        "author_short": "Stibel",
        "journal": "Brain, Behavior and Evolution",
        "volume": "98", "issue": "2", "pages": "93–106", "year": 2023,
        "doi": "10.1159/000528710",
        "url": "https://karger.com/bbe/article/98/2/93/835670/Climate-Change-Influences-Brain-Size-in-Humans",
        "license": "CC BY-NC 4.0", "license_url": "https://creativecommons.org/licenses/by-nc/4.0/",
        "oa": "Open access (non-commercial licence; publisher scopes the licence to the online version)",
        "dates": ("Received 26 May 2022; accepted 12 Dec 2022; published online 27 Dec 2022. "
                  "The publisher's own page also displays 3 April 2023 in the citation block and "
                  "22 June 2023 in the article-navigation header."),
        "type": "Original research",
        "role": "Tests climate as an environmental driver of brain size across the last 50,000 years.",
        "abstract": (
            "Brain size evolution in hominins constitutes a crucial evolutionary trend, yet the "
            "underlying mechanisms behind those changes are not well understood. Here, climate change "
            "is considered as an environmental factor using multiple paleoclimate records testing "
            "temperature, humidity, and precipitation against changes to brain size in 298 Homo "
            "specimens over the past fifty thousand years. Across regional and global paleoclimate "
            "records, brain size in Homo averaged significantly lower during periods of climate "
            "warming as compared to cooler periods. Geological epochs displayed similar patterns, "
            "with Holocene warming periods comprising significantly smaller brained individuals as "
            "compared to those living during glacial periods at the end of the Late Pleistocene. "
            "Testing spatiotemporal patterns, the adaptive response appears to have started roughly "
            "fifteen thousand years ago and may persist into modern times. To a smaller degree, "
            "humidity and precipitation levels were also predictive of brain size, with arid periods "
            "associated with greater brain size in Homo. The findings suggest an adaptive response to "
            "climate change in human brain size that is driven by natural selection in response to "
            "environmental stress."),
        "findings": [
            "Sample: <strong>298 <em>Homo</em> specimens</strong>, 373 independent cranial capacity measurements, spanning the past 50,000 years.",
            "Brain size shows an inverse relationship with temperature (least-squares regression <em>r</em> = −0.362, <em>p</em> &lt; 0.0001), holding after controlling for geography, sex and taxon (ANCOVA, <em>p</em> &lt; 0.0001).",
            "Specimens from cooler periods average <strong>1,426.31 g ± 137.30</strong> (n = 65) versus <strong>1,280.89 g ± 141.67</strong> (n = 233) in warmer periods — roughly a <strong>10.74% difference</strong> (<em>p</em> &lt; 0.0001).",
            "By epoch: Pleistocene 1,426.96 g ± 139.28 (n = 63) versus Holocene 1,281.95 g ± 141.58 (n = 235), a <strong>10.71% difference</strong>.",
            "Restricted to anatomically modern <em>Homo</em> (n = 289), the cool-period advantage is <strong>11.02%</strong>.",
            "Humidity and precipitation are weaker predictors: 5.28% for humidity (<em>p</em> &lt; 0.002) and 2.74% for precipitation (non-significant, <em>p</em> = 0.061).",
            "Covariate models explain roughly <strong>40–42%</strong> of variation — the paper is explicit that most variation remains unaccounted for.",
        ],
        "limitations": [
            "The paper states plainly that its data &ldquo;can only provide correlational support for spatiotemporal relationships&rdquo; and that future work is needed to confirm responsiveness of brain size to climate.",
            "Causal direction is unresolved: the author notes it is unclear whether brain size was selected on directly, or drifted alongside body size under selection.",
            "Sampling biases are disclosed — 220 of 298 specimens are high-latitude, and 167 of 257 sexed specimens are male.",
            "Climate accounts for only a small share of total variation in brain size; the paper says brain size adaptations &ldquo;are likely driven by other factors.&rdquo;",
            "The paper notes in its own Results that the climate and brain size records &ldquo;do not appear to correspond temporally,&rdquo; and that the linear relationship is confounded by differences across time series and cubic trends.",
            "No significant differences appear at temperature extremes (all <em>p</em> &gt; 0.50), only across moderate ranges.",
            "Humidity and precipitation records used are localized to Africa, and aridity there correlates with cooler conditions, so the effect may be mediated by temperature.",
        ],
    },

    "stibel2023body": {
        "key": "stibel2023body",
        "slug": "stibel-2023-body-size-proportionality",
        "title": "Climate Change Predictive of Body Size and Proportionality in Humans",
        "authors": ["Jeffrey M. Stibel"],
        "author_short": "Stibel",
        "journal": "Evolutionary Biology",
        "volume": "50", "issue": "4", "pages": "461–475", "year": 2023,
        "doi": "10.1007/s11692-023-09616-1",
        "url": "https://link.springer.com/article/10.1007/s11692-023-09616-1",
        "license": "CC BY 4.0", "license_url": "https://creativecommons.org/licenses/by/4.0/",
        "oa": "Open access. Author-deposited open copy available at Zenodo.",
        "open_copy": "https://zenodo.org/records/21969862",
        "open_copy_label": "Zenodo (author deposit, CC BY 4.0)",
        "dates": "Received 14 Feb 2023; accepted 25 Aug 2023; published online 3 Oct 2023",
        "type": "Original research",
        "role": "Extends the climate analysis to body mass and body shape across 700,000 years.",
        "abstract": (
            "The effects of climate change on plants and animals have been examined across numerous "
            "species, yet little evidence has been produced to demonstrate an influence on human "
            "evolution. Here the impact of climate change on human body size and scaling is examined "
            "over a period of 700,000 years using five independent paleoclimate records. Across 247 "
            "Homo specimens, body mass averaged significantly smaller during periods of climatic "
            "warming as compared to cooler cycles. Body proportions also changed significantly, "
            "appearing more ectomorphic during warmer periods and more endomorphic during periods of "
            "cooling across a sample of 87 specimens. The results indicate a relationship between "
            "climate change and body size and shape in humans that is driven by natural selection in "
            "response to thermoregulatory demands. The findings suggest that body size adaptations in "
            "response to climate change occurred early and potentially implicated cultural adaptations "
            "in later periods, muting the morphological response to extreme climates. Because "
            "morphological variation has been used as a factor for classification within the genus "
            "Homo, taxonomic and phylogenic decisions may need to be reconsidered in the context of "
            "temporal climate differences."),
        "findings": [
            "Sample: <strong>247 <em>Homo</em> specimens</strong> across 700,000 years, against five independent paleoclimate records.",
            "Body mass in cooler periods averages <strong>66.40 kg ± 0.86</strong> versus <strong>59.00 kg ± 0.73</strong> in warmer periods — a <strong>11.8% difference</strong>.",
            "Roughly <strong>half</strong> of total body mass variation is accounted for by the model (<em>r</em>² = 0.51 for <em>Homo</em>; 0.53 for anatomically modern humans, both <em>p</em> &lt; 0.0001).",
            "Body <em>shape</em> also shifts: stature-to-body-mass ratio is 7.09% greater in warmer cycles (<em>p</em> &lt; 0.01), rising to 9.89% at 10,000-year averaging.",
            "Stature alone shows <strong>no</strong> significant difference across temperature cycles (<em>p</em> = 0.07) — climate affects mass and proportion, not height.",
            "The pattern replicates across independent records: East African (Lake Malawi) 12.53%, North Atlantic deep-sea 11.04%, African fossils only 13.59%.",
            "The author raises a taxonomic implication: because morphology is used to classify within <em>Homo</em>, some species boundaries may partly reflect climate rather than phylogeny.",
        ],
        "limitations": [
            "The proportionality sample is small (87 specimens) and biased toward high-latitude (82 of 87) males (41 of 73 sexed specimens).",
            "Testing proportionality is &ldquo;approximate at best&rdquo; — each metric used has known weaknesses, and results using the Ponderal Index were <em>not</em> significant.",
            "The author notes the proportionality effect may be an artifact of the strong body-mass effect rather than an independent shape response.",
            "Effects disappear at temperature extremes (<em>p</em> &gt; 0.09), and tail effects may reflect outliers — two Late Pleistocene East Asian groups and five Neanderthals.",
            "Alternative drivers are acknowledged: precipitation, humidity, extreme weather, vegetation, water availability, or non-climate factors such as culture and technology.",
        ],
    },

    "stibel2021": {
        "key": "stibel2021",
        "slug": "stibel-2021-encephalization-decline",
        "title": "Decreases in Brain Size and Encephalization in Anatomically Modern Humans",
        "authors": ["Jeff Morgan Stibel"],
        "author_short": "Stibel",
        "journal": "Brain, Behavior and Evolution",
        "volume": "96", "issue": "2", "pages": "64–77", "year": 2021,
        "doi": "10.1159/000519504",
        "url": "https://karger.com/bbe/article/96/2/64/821534/Decreases-in-Brain-Size-and-Encephalization-in",
        "license": "CC BY-NC 4.0", "license_url": "https://creativecommons.org/licenses/by-nc/4.0/",
        "oa": "Open access (non-commercial licence). Author-deposited open copy available at Zenodo.",
        "open_copy": "https://zenodo.org/records/21970102",
        "open_copy_label": "Zenodo (author deposit, CC BY-NC 4.0)",
        "dates": ("Received 24 Jan 2021; accepted 28 Aug 2021; published online 29 Oct 2021; "
                  "citation block dates the issue 6 December 2021"),
        "type": "Original research",
        "role": "Asks whether brain size decline is proportional to body size decline — and finds most of it is.",
        "abstract": (
            "Growth in human brain size and encephalization is well documented throughout much of "
            "prehistory and believed to be responsible for increasing cognitive faculties. Over the "
            "past 50,000 years, however, both body size and brain mass have decreased but little is "
            "known about the scaling relationship between the two. Here, changes to the human brain "
            "are examined using matched body remains to determine encephalization levels across an "
            "evolutionary timespan. The results find decreases to encephalization levels in modern "
            "humans as compared to earlier Holocene H. sapiens and Late Pleistocene anatomically "
            "modern Homo. When controlled for lean body mass, encephalization changes are isometric, "
            "suggesting that much of the declines in encephalization are driven by recent increases in "
            "obesity. A meta-review of genome-wide association studies finds some evidence for "
            "selective pressures acting on human cognitive ability, which may be an evolutionary "
            "consequence of the more than 5% loss in brain mass over the past 50,000 years."),
        "findings": [
            "Brain size has declined <strong>5.415%</strong> in modern humans relative to the Upper Paleolithic (~50–15 kyr BP), <em>p</em> &lt; 0.001.",
            "The modern sample is <strong>17% less encephalized</strong> than the <em>H. sapiens</em> comparison sample (<em>p</em> &lt; 0.001).",
            "Critically: when controlled for <strong>lean</strong> body mass, encephalization change is <strong>isometric</strong> — much of the apparent decline tracks modern obesity, not neural reduction.",
            "The modern sample's mean BMI is <strong>25.3</strong> (overweight range). BMI and encephalization quotient correlate at <em>r</em> = 0.84 (<em>p</em> &lt; 0.0001) in that sample.",
            "The brain–body mass relationship across earlier groups (<em>r</em> = 0.66 Plio/Pleistocene hominins, 0.82 Late Pleistocene, but only 0.43 Early Holocene) <strong>breaks down</strong> in the modern sample (<em>r</em> = 0.08, <em>p</em> = 0.75).",
            "Encephalization trend reverses sign: <em>r</em> = 0.777 across the prehistoric record versus <em>r</em> = −0.483 over the past 1,000 years.",
            "Sample: 30 Holocene and 25 Late Pleistocene anatomically modern <em>Homo</em>, 16 older hominins, and autopsy data from 19 deceased individuals.",
        ],
        "limitations": [
            "The modern comparison rests on autopsy data from only <strong>19 individuals</strong> (11 German, 8 Australian Aboriginal males, all deceased 1980–82) — a small and unrepresentative modern sample.",
            "The author's own framing of the proxy: &ldquo;The link between brain size and cognitive ability is spurious at best, but the relationship appears to hold strong validity when looked at with regards to evolutionary changes within species.&rdquo; The first clause is widely quoted in isolation; the second clause is the one that applies to this literature.",
            "Encephalization is used as the cognitive proxy while the paper acknowledges this ignores neuron count, neuronal density, interneuron distance, axonal conduction velocity and cortex scaling.",
            "Specimens were grouped by time period irrespective of sex or geography because of limited fossil and autopsy availability.",
            "The genome-wide association datasets reviewed are &ldquo;limited to western cultures and not representative of the global population.&rdquo;",
            "Cognitive ability measures are noted to be culturally, environmentally and educationally biased.",
        ],
    },

    "stibel2025": {
        "key": "stibel2025",
        "slug": "stibel-2025-brain-size-extinction-risk",
        "title": "Did increasing brain size place early humans at risk of extinction?",
        "authors": ["Jeffrey M. Stibel"],
        "author_short": "Stibel",
        "journal": "Brain and Cognition",
        "volume": "188", "pages": "106336", "year": 2025,
        "doi": "10.1016/j.bandc.2025.106336",
        "url": "https://www.sciencedirect.com/science/article/pii/S0278262625000764",
        "license": "CC BY 4.0", "license_url": "https://creativecommons.org/licenses/by/4.0/",
        "oa": "Hybrid open access. Author-deposited open copy available at Zenodo.",
        "open_copy": "https://zenodo.org/records/21968809",
        "open_copy_label": "Zenodo (author deposit, CC BY 4.0)",
        "dates": "Received 25 Oct 2024; revised and accepted 3 Jul 2025; online 15 Jul 2025; issue 1 Aug 2025",
        "type": "Original research (special issue: environmental effects on brain and cognition)",
        "role": "Reframes the question — not why brains shrank recently, but why they stopped growing ~300,000 years ago.",
        "abstract": (
            "Increasing brain size is a hallmark of human evolution. While a larger brain offers "
            "evolutionary advantages driven by social and cognitive adaptations, it also imposes "
            "considerable energetic, metabolic, and thermoregulatory costs. As a result, brain size may "
            "have biological limits that impose survival pressures during periods of extreme "
            "environmental change. Here, temporal trends in absolute brain size across the genus Homo "
            "are analyzed, with a focus on a marked slowdown in growth beginning around 300,000 years "
            "ago. The results suggest that strong directional selection for brain expansion in early "
            "Homo was followed by a shift toward stabilizing selection in later populations. "
            "Comparisons across glacial and interglacial periods indicate that the physiological costs "
            "of large brains may have become especially disadvantageous during warming interglacial "
            "periods in the last 100,000 years, potentially increasing extinction risk. This "
            "evolutionary shift coincides with the emergence of cognitive and cultural innovations—such "
            "as symbolic tools and language—that may have enabled cognitive offloading, reducing "
            "selective pressure for continued encephalization. Together, these findings support the "
            "hypothesis that stabilizing selection, mediated in part by behavioral and technological "
            "adaptations, buffered later Homo populations against the ecological and physiological "
            "costs associated with large brains."),
        "findings": [
            "Sample: <strong>800 cranial capacity measurements</strong> across the genus <em>Homo</em>, including 690 <em>H. sapiens</em> and 99 individuals across eight paleospecies.",
            "Brain size growth shows <strong>no significant trend after roughly 300,000 years ago</strong> — the expansion plateaus (Kruskal–Wallis <em>H</em> = 135.08, <em>p</em> &lt; 0.0001 across bins).",
            "Glacial–interglacial differences appear <strong>only in the last 100,000 years</strong> (<em>p</em> &lt; 0.0001); there is no such difference between 100–300 kyr BP (<em>p</em> = 0.923).",
            "Factorial ANOVA finds significant effects of time (<em>F</em> = 208.22), climate stage (<em>F</em> = 44.73), and their interaction (<em>F</em> = 5.17), all <em>p</em> &lt; 0.0001.",
            "The energetic case: brains account for roughly <strong>20% of adult resting energy consumption and up to 60% in early development</strong>.",
            "The offloading chronology: symbolic objects appear 100,000–150,000 years ago — Bizmoune Cave shell beads (~142–100 kya), Blombos Cave engraved ochre (~100–75 kya), Diepkloof ostrich eggshell (~65 kya), systematic notation (~50 kya).",
            "Interpretation offered: directional selection for expansion gave way to <strong>stabilizing selection</strong>, with cognitive tools relieving pressure for further encephalization.",
        ],
        "limitations": [
            "The author states the trend &ldquo;is not strictly monotonic and should be interpreted cautiously&rdquo; — significant pairwise differences cluster in the oldest and most recent periods.",
            "Finer temporal bins lacked sufficient sample sizes for robust glacial–interglacial comparison.",
            "Sample sizes within the genus <em>Homo</em> are low, requiring model-free curve fitting and coarse binning to accommodate dating uncertainty.",
            "Taxonomically contested specimens (<em>H. floresiensis</em>, <em>H. naledi</em>) were tested in and out; results did not change in direction or significance.",
            "The cognitive offloading account is an interpretation consistent with the chronology, not a directly tested causal result.",
        ],
        "note": (
            "This paper does not discuss consciousness, machine intelligence, or the extended mind "
            "thesis. Artificial intelligence appears once, as a modern analogy for cognitive offloading. "
            "Claims to the contrary misrepresent it."),
    },

    # ------------------------------------------------------- the opposing record
    "desilva2021": {
        "key": "desilva2021",
        "slug": "desilva-2021-change-point-ants",
        "title": ("When and Why Did Human Brains Decrease in Size? A New Change-Point Analysis "
                  "and Insights From Brain Evolution in Ants"),
        "authors": ["Jeremy M. DeSilva", "James F. A. Traniello",
                    "Alexander G. Claxton", "Luke D. Fannin"],
        "author_short": "DeSilva et al.",
        "journal": "Frontiers in Ecology and Evolution",
        "volume": "9", "pages": "742639", "year": 2021,
        "doi": "10.3389/fevo.2021.742639",
        "url": "https://www.frontiersin.org/articles/10.3389/fevo.2021.742639/full",
        "license": "CC BY 4.0", "license_url": "https://creativecommons.org/licenses/by/4.0/",
        "oa": "Gold open access",
        "type": "Original research",
        "role": "Round 1. The paper that started the modern exchange — change-point analysis placing a reduction at ~3,000 BP, with an analogy to eusocial insect colonies.",
        "lim_heading": "Subsequent response",
        "abstract": "",
        "findings": [
            "Change-point analysis on a large compilation of fossil and recent human crania places a brain size reduction at approximately <strong>3,000 years BP</strong>.",
            "Proposed mechanism: externalization of information into social groups and collective intelligence reduced selective pressure for individually large brains.",
            "Drew an explicit parallel to brain size reduction in eusocial ant colonies.",
        ],
        "limitations": [
            "The dataset and change-point timing were directly challenged the following year by Villmoare &amp; Grabowski (2022); see the debate page.",
        ],
    },

    "villmoare2022": {
        "key": "villmoare2022",
        "slug": "villmoare-grabowski-2022-reassessment",
        "title": ("Did the transition to complex societies in the Holocene drive a reduction in "
                  "brain size? A reassessment of the DeSilva et al. (2021) hypothesis"),
        "authors": ["Brian Villmoare", "Mark Grabowski"],
        "author_short": "Villmoare & Grabowski",
        "journal": "Frontiers in Ecology and Evolution",
        "volume": "10", "pages": "963568", "year": 2022,
        "doi": "10.3389/fevo.2022.963568",
        "url": "https://www.frontiersin.org/journals/ecology-and-evolution/articles/10.3389/fevo.2022.963568/full",
        "license": "CC BY 4.0", "license_url": "https://creativecommons.org/licenses/by/4.0/",
        "oa": "Gold open access",
        "dates": "Published 29 July 2022",
        "type": "Opinion article",
        "role": "Round 2. The rebuttal, and the most widely circulated source on this topic.",
        "lim_heading": "Subsequent response",
        "abstract": "",
        "findings": [
            "Reanalyzing portions of the DeSilva et al. dataset, the authors detect <strong>no reduction in brain size</strong> in modern humans over any period since the origin of the species (~300,000 years).",
            "Criticism 1: the dataset pools specimens from radically different populations and geographies (England, China, Mali, Algeria) as if directly comparable.",
            "Criticism 2: only <strong>23 crania</strong> fall within the time window critical to the hypothesis.",
            "Criticism 3: 578 of the ~987 specimens represent only the last 100 years of a ~9.8-million-year span, skewing the change-point estimate toward the recent.",
            "Criticism 4 &mdash; arguably their strongest: the modern human mean generated by the original dataset (~1,297 cc) sits <strong>well below</strong> other published estimates, which range from ~1,340 cc to ~1,460 cc. If the modern anchor is set too low, an apparent decline is an artefact of the reference value rather than a real trend.",
            "Criticism 5: the original change point was never significance-tested. Applying a Davies (1987) test, the authors find <strong>no significant change point</strong> near 3 ka (<em>p</em> = 0.621 on the full data; 0.739 at 300 ka; 0.259 at 30 ka), and document violated regression assumptions.",
            "Their summary position: human brain size has been &ldquo;remarkably stable over the last 300 ka.&rdquo;",
        ],
        "limitations": [
            "DeSilva et al. (2023) responded that a significant Holocene reduction persists in a corrected dataset, while conceding the sampling-skew point.",
        ],
    },

    "decaro2024": {
        "key": "decaro2024",
        "slug": "de-caro-2024-commentary",
        "title": "Commentary: Human brains have shrunk: the questions are when and why",
        "authors": ["Liberato De Caro"],
        "author_short": "De Caro",
        "journal": "Frontiers in Ecology and Evolution",
        "year": 2024,
        "doi": "10.3389/fevo.2024.1368347",
        "url": "https://www.frontiersin.org/journals/ecology-and-evolution/articles/10.3389/fevo.2024.1368347/full",
        "license": "CC BY 4.0", "license_url": "https://creativecommons.org/licenses/by/4.0/",
        "oa": "Gold open access",
        "dates": "Published 11 April 2024",
        "type": "Commentary",
        "role": "Round 4. A published commentary responding to the 2023 paper — the most recent entry in the exchange.",
        "abstract": "",
        "findings": [],
        "limitations": [],
    },

    "hawks2011": {
        "key": "hawks2011",
        "slug": "hawks-2011-selection-smaller-brains",
        "title": "Selection for smaller brains in Holocene human evolution",
        "authors": ["John Hawks"],
        "author_short": "Hawks",
        "journal": "arXiv preprint",
        "year": 2011,
        "doi": "",
        "url": "https://arxiv.org/abs/1102.5604",
        "license": "arXiv licence", "license_url": "",
        "oa": "Freely available preprint",
        "type": "Preprint",
        "role": "Independent prior work arguing for Holocene selection toward smaller brains — predates the current exchange and is cited by both sides.",
        "abstract": "",
        "findings": [],
        "limitations": [],
    },

    "henneberg1988": {
        "key": "henneberg1988",
        "slug": "henneberg-1988-skull-size-holocene",
        "title": "Decrease of human skull size in the Holocene",
        "authors": ["Maciej Henneberg"],
        "author_short": "Henneberg",
        "journal": "Human Biology",
        "volume": "60", "issue": "3", "pages": "395–405", "year": 1988,
        "doi": "",
        "url": "https://www.jstor.org/stable/41464021",
        "license": "All rights reserved", "license_url": "",
        "oa": "Paywalled",
        "type": "Original research",
        "role": "The roughly 90-year-old observational baseline that both sides of the modern dispute invoke.",
        "abstract": "",
        "findings": [],
        "limitations": [],
    },

    "will2021": {
        "key": "will2021",
        "slug": "will-2021-climate-body-brain-size",
        "title": "Different environmental variables predict body and brain size evolution in Homo",
        "authors": ["Manuel Will", "Mario Krapp", "Jay T. Stock", "Andrea Manica"],
        "author_short": "Will et al.",
        "journal": "Nature Communications",
        "volume": "12", "pages": "4116", "year": 2021,
        "doi": "10.1038/s41467-021-24290-7",
        "url": "https://www.nature.com/articles/s41467-021-24290-7",
        "license": "CC BY 4.0", "license_url": "https://creativecommons.org/licenses/by/4.0/",
        "oa": "Open access",
        "type": "Original research",
        "role": "Independent team, convergent question: finds climate a strong predictor of body size in Homo but only a weak and indirect predictor of brain size.",
        "abstract": "",
        "findings": [
            "Temperature is a major predictor of body size variation in <em>Homo</em> over the past million years.",
            "Environmental predictors of <strong>brain</strong> size are weaker and differ from those for body size — the authors find brain size better predicted by non-climatic factors.",
        ],
        "limitations": [],
    },
}

# Papers authored or co-authored within the portfolio being disseminated
CORE_FIVE = ["stibel2021", "stibel2023climate", "stibel2023body", "desilva2023", "stibel2025"]

# Everything else cited in the hub, for the sources page
CONTEXT_PAPERS = ["desilva2021", "villmoare2022", "decaro2024", "hawks2011",
                  "henneberg1988", "will2021"]


def citation(p):
    """Render a plain citation string."""
    a = p["authors"]
    if len(a) == 1:
        names = a[0]
    elif len(a) <= 3:
        names = ", ".join(a[:-1]) + " & " + a[-1]
    else:
        names = a[0] + " et al."
    bits = [f"{names} ({p['year']}). {p['title']}."]
    if p.get("journal"):
        j = f"<em>{p['journal']}</em>"
        if p.get("volume"):
            j += f", {p['volume']}"
            if p.get("issue"):
                j += f"({p['issue']})"
        if p.get("pages"):
            j += f", {p['pages']}"
        bits.append(j + ".")
    if p.get("doi"):
        bits.append(f'DOI: <a href="https://doi.org/{p["doi"]}">{p["doi"]}</a>')
    return " ".join(bits)
