# -*- coding: utf-8 -*-
"""
Verified bibliographic record for every paper cited in the hub.

Every field here was read off the publisher's own page or PDF during the
2026-08-15 verification pass. Nothing in this file is from recall.
Where a publisher states conflicting values (Karger gives three different
publication dates for BBE 98(2)), the conflict is recorded rather than resolved.
"""
import re

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
        "role": "Round 3 of the Holocene brain size exchange, the authors' response to Villmoare & Grabowski (2022).",
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
            "The result holds when the authors' own sample is tested against two independent modern reference datasets (Dekaban &amp; Sadowsky n = 3,399, <em>t</em> = 9.83; Beals et al. n = 5,288, <em>t</em> = 9.04; both <em>p</em> &lt; 0.0001).",
            "Framed as effect size: human brain volume has decreased by roughly <strong>one standard deviation</strong> in the last 10,000 years, whether examined locally or globally.",
        ],
        "limitations": [
            "The authors concede the Holocene portion of the original dataset is skewed toward modern specimens, an unavoidable taphonomic bias that may pull the change-point estimate too recent and could obscure earlier change points.",
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
            "Specimens from cooler periods average <strong>1,426.31 g ± 137.30</strong> (n = 65) versus <strong>1,280.89 g ± 141.67</strong> (n = 233) in warmer periods, roughly a <strong>10.74% difference</strong> (<em>p</em> &lt; 0.0001).",
            "By epoch: Pleistocene 1,426.96 g ± 139.28 (n = 63) versus Holocene 1,281.95 g ± 141.58 (n = 235), a <strong>10.71% difference</strong>.",
            "Restricted to anatomically modern <em>Homo</em> (n = 289), the cool-period advantage is <strong>11.02%</strong>.",
            "Humidity and precipitation are weaker predictors: 5.28% for humidity (<em>p</em> &lt; 0.002) and 2.74% for precipitation (non-significant, <em>p</em> = 0.061).",
            "Covariate models explain roughly <strong>40–42%</strong> of variation, the paper is explicit that most variation remains unaccounted for.",
        ],
        "limitations": [
            "The paper states plainly that its data &ldquo;can only provide correlational support for spatiotemporal relationships&rdquo; and that future work is needed to confirm responsiveness of brain size to climate.",
            "Causal direction is unresolved: the author notes it is unclear whether brain size was selected on directly, or drifted alongside body size under selection.",
            "Sampling biases are disclosed, 220 of 298 specimens are high-latitude, and 167 of 257 sexed specimens are male.",
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
        "authors": ["Jeff Morgan Stibel"],
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
            "Body mass in cooler periods averages <strong>66.40 kg ± 0.86</strong> versus <strong>59.00 kg ± 0.73</strong> in warmer periods, a <strong>11.8% difference</strong>.",
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
            "Effects disappear at temperature extremes (<em>p</em> &gt; 0.09), and tail effects may reflect outliers, two Late Pleistocene East Asian groups and five Neanderthals.",
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
        "role": "Asks whether brain size decline is proportional to body size decline, and finds most of it is.",
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
        "authors": ["Jeff Morgan Stibel"],
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
        "role": "Reframes the question, not why brains shrank recently, but why they stopped growing ~300,000 years ago.",
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
            "Sample: <strong>800 cranial capacity measurements</strong> across the genus <em>Homo</em>. The paper reports 690 <em>H. sapiens</em> and 99 individuals across eight paleospecies; these subgroup figures do not sum to the stated total.",
            "Brain size growth shows <strong>no significant trend after roughly 300,000 years ago</strong> — the expansion plateaus (Kruskal–Wallis <em>H</em> = 135.08, <em>p</em> &lt; 0.0001 across bins).",
            "Glacial–interglacial differences appear <strong>only in the last 100,000 years</strong> (<em>p</em> &lt; 0.0001); there is no such difference between 100–300 kyr BP (<em>p</em> = 0.923).",
            "Factorial ANOVA finds significant effects of time (<em>F</em> = 208.22), climate stage (<em>F</em> = 44.73), and their interaction (<em>F</em> = 5.17), all <em>p</em> &lt; 0.0001.",
            "The energetic case: brains account for roughly <strong>20% of adult resting energy consumption and up to 60% in early development</strong>.",
            "The offloading chronology: symbolic objects appear 100,000–150,000 years ago, Bizmoune Cave shell beads (~142–100 kya), Blombos Cave engraved ochre (~100–75 kya), Diepkloof ostrich eggshell (~65 kya), systematic notation (~50 kya).",
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
        "role": "Round 1. The paper that started the modern exchange, change-point analysis placing a reduction at ~3,000 BP, with an analogy to eusocial insect colonies.",
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
        "volume": "12", "pages": "1368347",
        "year": 2024,
        "doi": "10.3389/fevo.2024.1368347",
        "url": "https://www.frontiersin.org/journals/ecology-and-evolution/articles/10.3389/fevo.2024.1368347/full",
        "license": "CC BY 4.0", "license_url": "https://creativecommons.org/licenses/by/4.0/",
        "oa": "Gold open access",
        "dates": "Published 11 April 2024",
        "type": "General commentary",
        "role": ("Round 4. A short commentary re-examining the DeSilva dataset for sex-representation "
                 "bias. It introduces no new specimens and works entirely from data published by "
                 "others."),
        "abstract": "",
        "findings": [
            "Recomputes a modern reference value from four sex-balanced datasets (Dekaban &amp; Sadowsky n = 3,399; Ho et al. n = 1,261; Beals et al. n = 5,288; plus DeSilva's n = 415), giving 1,341 &plusmn; 130 cc across n = 10,363.",
            "Argues that the 25 crania from Afalou, Algeria (~11.5 ka) are male-biased, estimated from histogram shape rather than osteological sexing, and should be excluded.",
            "Reports that the reduction across 5 ka &ge; age &gt; 0.15 ka holds with that subset removed.",
            "Fits a log-age regression to period means and argues the decline is continuous from the Late Pleistocene rather than beginning at 3&ndash;5 ka.",
            "Notes that the fit implies roughly 50 cc per log-decade against a within-species range near 1,000 cc, so most variance in the data is individual rather than temporal.",
        ],
        "limitations": [
            "The sex-balance inference for the Afalou sample is estimated from the shape of a histogram rather than from independent osteological sexing.",
            "The analysis works from means rather than individual specimens for the main fit, a choice De Caro defends as standard timeseries practice but which discards within-interval information.",
            "The reanalysis uses the DeSilva et al. (2023) dataset throughout and inherits its coverage gaps; De Caro calls for extension to datasets not considered there.",
        ],
        "lim_heading": "Limitations of this reanalysis",
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
        "oa": "Freely available preprint. Not peer reviewed.",
        "type": "Preprint (not peer reviewed)",
        "role": "An unrefereed preprint arguing for Holocene selection toward smaller brains. Cited by both sides of the current dispute, but it was never published in a peer-reviewed venue and is listed here with that caveat.",
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
        "role": "The 1988 observational baseline that both sides of the modern dispute invoke.",
        "findings": [
            "Reports a decrease in cranial capacity from the Mesolithic to modern times, derived from linear measurements on a large European skull series.",
            "Later extended to a sub-Saharan African sample by Henneberg &amp; Steyn (1993), testing whether the pattern was regional or general.",
        ],
        "limitations": [
            "An erratum was published the following year (<em>Human Biology</em> 61(3), 478, June 1989; recorded on PubMed PMID 3134287). Corrected values should be used. Neither the article nor the erratum has a DOI.",
            "The series is predominantly European, with limited additions from northwest Africa and west Asia.",
        ],
        "lim_heading": "Corrections and coverage",
        "abstract": "",
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
        "role": "Tests a wide set of environmental variables against body and brain size across a million years. Finds temperature a strong predictor of body size and only weak, probably indirect predictors of brain size.",
        "abstract": "",
        "findings": [
            "Temperature is a major predictor of body size variation in <em>Homo</em> over the past million years.",
            "Net primary productivity and long-term variability in precipitation correlate with <strong>brain</strong> size, but explain low amounts of the observed variation.",
            "The authors conclude that most environmental factors they test &ldquo;do not correspond with body and brain size evolution,&rdquo; and that the brain size relationships they do find are likely indirect.",
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
    bits = [f"{names} ({yr(p['key'])}). {p['title']}."]
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


# ---------------------------------------------------------------------------
# Wider literature. Verified against Crossref/OpenAlex/PubMed on 2026-08-16.
# These are cited inline throughout the site so that no page rests on a single
# study. Peer-reviewed only; preprints are excluded.
# ---------------------------------------------------------------------------

LIT = {
 # --- Holocene and recent cranial change -----------------------------------
 "henneberg1988": ("Henneberg, M. (1988). Decrease of human skull size in the Holocene. "
   "<em>Human Biology</em> 60(3), 395&ndash;405.", None,
   "The observation that anchors the whole discussion. An erratum was published the following year "
   "(<em>Hum Biol</em> 61(3):478); corrected values should be used."),
 "hennebergsteyn1993": ("Henneberg, M. &amp; Steyn, M. (1993). Trends in cranial capacity and cranial "
   "index in Subsaharan Africa during the Holocene. <em>American Journal of Human Biology</em> 5(4), "
   "473&ndash;479.", "10.1002/ajhb.1310050411",
   "Tests whether the Holocene decrease is global rather than European. Finds it in a sub-Saharan series."),
 "henneberg1998": ("Henneberg, M. (1998). Evolution of the human brain: is bigger better? "
   "<em>Clinical and Experimental Pharmacology and Physiology</em> 25(9), 745&ndash;749.",
   "10.1111/j.1440-1681.1998.tb02289.x",
   "The researcher who documented the decrease argues it carries no implication for cognitive capacity."),
 "beals1984": ("Beals, K.L., Smith, C.L. &amp; Dodd, S.M. (1984). Brain size, cranial morphology, "
   "climate, and time machines. <em>Current Anthropology</em> 25(3), 301&ndash;330.", "10.1086/203138",
   "The classic dataset relating cranial capacity to climate across populations. Published with "
   "commentary and reply, so the main objections sit alongside it in the record."),
 "miller1977": ("Miller, A.K.H. &amp; Corsellis, J.A.N. (1977). Evidence for a secular increase in "
   "human brain weight during the past century. <em>Annals of Human Biology</em> 4(3), 253&ndash;257.",
   "10.1080/03014467700007142",
   "Autopsy series showing brain weight rising across the twentieth century. A secular trend within "
   "living populations, on a timescale too short to be evolutionary."),
 "decarli2024": ("DeCarli, C., Maillard, P., Pase, M.P., Beiser, A.S., Kojis, D., Satizabal, C.L., "
   "Himali, J.J., Aparicio, H.J., Fletcher, E. &amp; Seshadri, S. (2024). Trends in intracranial and "
   "cerebral volumes of Framingham Heart Study participants born 1930 to 1970. "
   "<em>JAMA Neurology</em> 81(5), 471.", "10.1001/jamaneurol.2024.0469",
   "MRI across four birth decades finds intracranial and cerebral volumes increasing. Forty years "
   "spans roughly one and a half generations, so this measures growth conditions rather than "
   "selection."),
 "jantz2016": ("Jantz, R.L. &amp; Jantz, L.M. (2016). The remarkable change in Euro-American cranial "
   "shape and size. <em>Human Biology</em> 88(1), 56.", "10.13110/humanbiology.88.1.0056",
   "Substantial cranial change across roughly 150 years, far too fast for natural selection. Points "
   "to plasticity rather than evolutionary change in recent samples."),

 # --- Climate, latitude, body size -----------------------------------------
 "ruff1994": ("Ruff, C.B. (1994). Morphological adaptation to climate in modern and fossil hominids. "
   "<em>American Journal of Physical Anthropology</em> 37(S19), 65&ndash;107.", "10.1002/ajpa.1330370605",
   "The standard review of body form and climate in humans. Body breadth, not stature, is the "
   "climatically constrained dimension."),
 "ruff1997": ("Ruff, C.B., Trinkaus, E. &amp; Holliday, T.W. (1997). Body mass and encephalization in "
   "Pleistocene <em>Homo</em>. <em>Nature</em> 387(6629), 173&ndash;176.", "10.1038/387173a0",
   "Endocranial trends cannot be read without a matched body mass series, because body size changed too. "
   "The standard methodological objection to any brain size claim."),
 "katzmarzyk1998": ("Katzmarzyk, P.T. &amp; Leonard, W.R. (1998). Climatic influences on human body "
   "size and proportions. <em>American Journal of Physical Anthropology</em> 106(4), 483&ndash;503.",
   "10.1002/(SICI)1096-8644(199808)106:4<483::AID-AJPA4>3.0.CO;2-K",
   "Restudy of the classic climate-body size relationship across 418 samples. The slopes are shallower "
   "than in 1953, which the authors attribute to twentieth-century nutritional change."),
 "foster2013": ("Foster, F. &amp; Collard, M. (2013). A reassessment of Bergmann's rule in modern humans. "
   "<em>PLoS ONE</em> 8(8), e72269.", "10.1371/journal.pone.0072269",
   "Bergmann's rule holds in humans only across very wide latitude or temperature ranges. Earlier "
   "support came from hemisphere-biased samples."),
 "savell2016": ("Savell, K.R.R., Auerbach, B.M. &amp; Roseman, C.C. (2016). Constraint, natural "
   "selection, and the evolution of human body form. <em>PNAS</em> 113(34), 9492&ndash;9497.",
   "10.1073/pnas.1603632113",
   "Quantitative genetic modelling finds some limb clines are correlated side effects rather than "
   "adaptations. Group mean differences are poor evidence of adaptation."),
 "wells2012": ("Wells, J.C.K. (2012). Ecogeographical associations between climate and human body "
   "composition. <em>American Journal of Physical Anthropology</em> 147(2), 169&ndash;186.",
   "10.1002/ajpa.21591",
   "Across 137 non-industrialised populations the climate signal may run through fat rather than lean "
   "mass. Polynesian populations run counter to every trend."),

 # --- Energetics ------------------------------------------------------------
 "aiello1995": ("Aiello, L.C. &amp; Wheeler, P. (1995). The expensive-tissue hypothesis. "
   "<em>Current Anthropology</em> 36(2), 199&ndash;221.", "10.1086/204350",
   "Proposed that brain expansion was paid for by a reduced gut. The origin of the metabolic framing."),
 "navarrete2011": ("Navarrete, A., van Schaik, C.P. &amp; Isler, K. (2011). Energetics and the evolution "
   "of human brain size. <em>Nature</em> 480(7375), 91&ndash;93.", "10.1038/nature10629",
   "Across a large mammal sample, relative brain size and relative gut size do not trade off once fat "
   "is accounted for. Contradicts the expensive tissue hypothesis directly."),
 "fonseca2012": ("Fonseca-Azevedo, K. &amp; Herculano-Houzel, S. (2012). Metabolic constraint imposes "
   "tradeoff between body size and number of brain neurons in human evolution. <em>PNAS</em> 109(45), "
   "18571&ndash;18576.", "10.1073/pnas.1206390109",
   "Sets a feeding-time ceiling on how many neurons a primate can support at a given body size."),
 "kuzawa2014": ("Kuzawa, C.W., Chugani, H.T., Grossman, L.I., et al. (2014). Metabolic costs and "
   "evolutionary implications of human brain development. <em>PNAS</em> 111(36), 13010&ndash;13015.",
   "10.1073/pnas.1323099111",
   "Brain glucose use peaks in childhood at 66.3% of resting metabolic rate in males and 65.0% in "
   "females, and body growth slows as brain demand rises."),
 "pontzer2016": ("Pontzer, H., Brown, M.H., Raichlen, D.A., et al. (2016). Metabolic acceleration and "
   "the evolution of human brain size and life history. <em>Nature</em> 533(7603), 390&ndash;392.",
   "10.1038/nature17654",
   "Humans expanded the total energy budget rather than only reallocating within a fixed one, which "
   "complicates pure trade-off accounts."),
 "isler2009": ("Isler, K. &amp; van Schaik, C.P. (2009). The expensive brain: a framework for explaining "
   "evolutionary changes in brain size. <em>Journal of Human Evolution</em> 57(4), 392&ndash;400.",
   "10.1016/j.jhevol.2009.04.009",
   "Brain size is limited jointly by stable energy supply and by allocation away from growth and "
   "reproduction."),

 # --- Brain size and cognition ---------------------------------------------
 "pietschnig2015": ("Pietschnig, J., Penke, L., Wicherts, J.M., Zeiler, M. &amp; Voracek, M. (2015). "
   "Meta-analysis of associations between human brain volume and intelligence differences. "
   "<em>Neuroscience &amp; Biobehavioral Reviews</em> 57, 411&ndash;432.", "10.1016/j.neubiorev.2015.09.017",
   "88 studies, over 8,000 individuals, pooled r = .24. The authors conclude brain size is not an "
   "isomorphic proxy for intelligence."),
 "gignac2017": ("Gignac, G.E. &amp; Bates, T.C. (2017). Brain volume and intelligence: the moderating "
   "role of intelligence measurement quality. <em>Intelligence</em> 64, 18&ndash;29.",
   "10.1016/j.intell.2017.06.004",
   "Reanalysing the same data restricted to healthy adults with better IQ measures gives r near .40, "
   "with no evidence of publication bias. Directly contests the lower figure."),
 "nave2019": ("Nave, G., Jung, W.H., Karlsson Linn&eacute;r, R., Kable, J.W. &amp; Koellinger, P.D. "
   "(2019). Are bigger brains smarter? <em>Psychological Science</em> 30(1), 43&ndash;54.",
   "10.1177/0956797618808470",
   "Preregistered UK Biobank study, n = 13,608. Brain volume and fluid intelligence correlate at "
   "r = .19, around 2% of variance."),
 "logan2018": ("Logan, C.J., Avin, S., Boogert, N., et al. (2018). Beyond brain size. "
   "<em>Comparative Cognition &amp; Behavior Reviews</em> 13, 55&ndash;89.", "10.3819/ccbr.2018.130008",
   "Gross volume conflates independently evolving components. Organisation, connectivity and neuron "
   "density carry the explanatory weight."),
 "smaers2021": ("Smaers, J.B., Rothman, R.S., Hudson, D.R., et al. (2021). The evolution of mammalian "
   "brain size. <em>Science Advances</em> 7(18), eabe2101.", "10.1126/sciadv.abe2101",
   "Across roughly 1,400 mammals, brain-body scaling slopes differ by clade and over time, so a single "
   "encephalization formula is not comparable across lineages."),
 "deaner2007": ("Deaner, R.O., Isler, K., Burkart, J. &amp; van Schaik, C. (2007). Overall brain size, "
   "and not encephalization quotient, best predicts cognitive ability across non-human primates. "
   "<em>Brain, Behavior and Evolution</em> 70(2), 115&ndash;124.", "10.1159/000102973",
   "Undercuts encephalization quotient as the standard comparative measure."),
 "trahan2014": ("Trahan, L.H., Stuebing, K.K., Fletcher, J.M. &amp; Hiscock, M. (2014). The Flynn effect: "
   "a meta-analysis. <em>Psychological Bulletin</em> 140(5), 1332&ndash;1360.", "10.1037/a0037173",
   "285 studies covering 1951 to 2010. Gains of roughly 2.9 to 3 IQ points per decade."),
 "bratsberg2018": ("Bratsberg, B. &amp; Rogeberg, O. (2018). Flynn effect and its reversal are both "
   "environmentally caused. <em>PNAS</em> 115(26), 6674&ndash;6678.", "10.1073/pnas.1718793115",
   "Norwegian conscript data recover the rise, the turning point and the decline entirely from "
   "within-family variation, leaving no room for a biological explanation."),
 "herculano2009": ("Herculano-Houzel, S. (2009). The human brain in numbers. "
   "<em>Frontiers in Human Neuroscience</em> 3, 31.", "10.3389/neuro.09.031.2009",
   "Counts rather than estimates the cells in the human brain, and finds it a linearly scaled-up "
   "primate brain."),

 # --- Offloading and distributed cognition ---------------------------------
 "risko2016": ("Risko, E.F. &amp; Gilbert, S.J. (2016). Cognitive offloading. "
   "<em>Trends in Cognitive Sciences</em> 20(9), 676&ndash;688.", "10.1016/j.tics.2016.07.002",
   "The defining review. Treats offloading as adaptive strategy selection rather than decline."),
 "sparrow2011": ("Sparrow, B., Liu, J. &amp; Wegner, D.M. (2011). Google effects on memory. "
   "<em>Science</em> 333(6043), 776&ndash;778.", "10.1126/science.1207745",
   "The most-cited experimental basis for the claim that search engines change memory."),
 "hesselmann2020": ("Hesselmann, G. (2020). No conclusive evidence that difficult general knowledge "
   "questions cause a Google Stroop effect. <em>PeerJ</em> 8, e10325.", "10.7717/peerj.10325",
   "Preregistered direct replication of Sparrow et al. The effect did not replicate."),
 "ward2017": ("Ward, A.F., Duke, K., Gneezy, A. &amp; Bos, M.W. (2017). Brain drain. "
   "<em>Journal of the Association for Consumer Research</em> 2(2), 140&ndash;154.", "10.1086/691462",
   "Reported that a nearby smartphone reduces available working memory."),
 "ruizpardo2022": ("Ruiz Pardo, A.C. &amp; Minda, J.P. (2022). Reexamining the brain drain effect. "
   "<em>Acta Psychologica</em> 230, 103717.", "10.1016/j.actpsy.2022.103717",
   "Preregistered replication across six conditions. No effect found."),
 "parry2023": ("Parry, D.A. (2023). Does the mere presence of a smartphone impact cognitive performance? "
   "<em>Media Psychology</em> 27(5), 737&ndash;762.", "10.1080/15213269.2023.2286647",
   "Meta-analysis finding null effects for most cognitive functions."),
 "bottger2023": ("B&ouml;ttger, T., Poschik, M. &amp; Zierer, K. (2023). Does the brain drain effect "
   "really exist? A meta-analysis. <em>Behavioral Sciences</em> 13(9), 751.", "10.3390/bs13090751",
   "Meta-analysis of the same literature reaching the opposite conclusion to Parry."),
 "grinschgl2021": ("Grinschgl, S., Papenmeier, F. &amp; Meyerhoff, H.S. (2021). Consequences of "
   "cognitive offloading. <em>Quarterly Journal of Experimental Psychology</em> 74(9), 1477&ndash;1496.",
   "10.1177/17470218211008060",
   "Offloading improves immediate performance and worsens later memory for the offloaded content. "
   "Reallocation rather than loss."),
 "storm2015": ("Storm, B.C. &amp; Stone, S.M. (2015). Saving-enhanced memory. "
   "<em>Psychological Science</em> 26(2), 182&ndash;188.", "10.1177/0956797614559285",
   "Saving one file before studying another improves memory for the second."),
 "muthukrishna2016": ("Muthukrishna, M. &amp; Henrich, J. (2016). Innovation in the collective brain. "
   "<em>Philosophical Transactions of the Royal Society B</em> 371(1690), 20150192.",
   "10.1098/rstb.2015.0192",
   "Innovation rate depends on population size, connectedness and transmission fidelity rather than "
   "individual intelligence."),
 "clark1998": ("Clark, A. &amp; Chalmers, D.J. (1998). The extended mind. <em>Analysis</em> 58(1), "
   "7&ndash;19.", "10.1093/analys/58.1.7",
   "The philosophical claim that cognitive processes can extend into the environment."),
 "sterelny2010": ("Sterelny, K. (2010). Minds: extended or scaffolded? "
   "<em>Phenomenology and the Cognitive Sciences</em> 9(4), 465&ndash;481.", "10.1007/s11097-010-9174-y",
   "Argues scaffolding explains the same evidence without the metaphysical commitments of extension."),
 "malafouris2019": ("Malafouris, L. (2019). Mind and material engagement. "
   "<em>Phenomenology and the Cognitive Sciences</em> 18(1), 1&ndash;17.", "10.1007/s11097-018-9606-7",
   "Material engagement theory: things participate in cognition rather than merely recording it."),

 # --- Self-domestication and gracilization ---------------------------------
 "cieri2014": ("Cieri, R.L., Churchill, S.E., Franciscus, R.G., Tan, J. &amp; Hare, B. (2014). "
   "Craniofacial feminization, social tolerance, and the origins of behavioral modernity. "
   "<em>Current Anthropology</em> 55(4), 419&ndash;443.", "10.1086/677209",
   "Documents brow ridge reduction and facial shortening from the Middle Pleistocene onward, and links "
   "it to selection for social tolerance."),
 "hare2017": ("Hare, B. (2017). Survival of the friendliest. <em>Annual Review of Psychology</em> 68(1), "
   "155&ndash;186.", "10.1146/annurev-psych-010416-044201",
   "The self-domestication case: selection for prosociality produces a suite of traits including "
   "reduced skeletal robusticity."),
 "wilkins2014": ("Wilkins, A.S., Wrangham, R.W. &amp; Fitch, W.T. (2014). The domestication syndrome in "
   "mammals. <em>Genetics</em> 197(3), 795&ndash;808.", "10.1534/genetics.114.165423",
   "Proposes mild neural crest deficits as the developmental route from selection for tameness to "
   "smaller brains and shorter faces."),
 "kruska2005": ("Kruska, D.C.T. (2005). On the evolutionary significance of encephalization in some "
   "eutherian mammals. <em>Brain, Behavior and Evolution</em> 65(2), 73&ndash;108.", "10.1159/000082979",
   "Domesticated mammals show brain size reductions of roughly 8 to 30 percent, and returning them to "
   "the wild does not restore it."),
 "sanchez2019": ("S&aacute;nchez-Villagra, M.R. &amp; van Schaik, C.P. (2019). Evaluating the "
   "self-domestication hypothesis of human evolution. <em>Evolutionary Anthropology</em> 28(3), "
   "133&ndash;143.", "10.1002/evan.21777",
   "Concludes the evidence that humans show the domestication trait set is weaker and more equivocal "
   "than the popular framing suggests."),
 "leach2003": ("Leach, H.M. (2003). Human domestication reconsidered. <em>Current Anthropology</em> "
   "44(3), 349&ndash;368.", "10.1086/368119",
   "Offers an alternative route to gracilization through the shared dietary and activity changes of "
   "sedentism, without invoking self-domestication."),

 # --- Archaic and Neanderthal comparisons ----------------------------------
 "neubauer2018": ("Neubauer, S., Hublin, J.-J. &amp; Gunz, P. (2018). The evolution of modern human "
   "brain shape. <em>Science Advances</em> 4(1), eaao5961.", "10.1126/sciadv.aao5961",
   "Endocranial volume was already within the modern range in the earliest <em>H. sapiens</em> around "
   "300,000 years ago. What changed afterwards was shape, not size."),
 "poncedeleon2021": ("Ponce de Le&oacute;n, M.S., Bienvenu, T., Marom, A., et al. (2021). The primitive "
   "brain of early <em>Homo</em>. <em>Science</em> 372(6538), 165&ndash;171.", "10.1126/science.aaz0032",
   "Separates brain reorganisation from brain enlargement. Ape-like frontal organisation persisted well "
   "after the genus originated."),
 "du2018": ("Du, A., Zipkin, A.M., Hatala, K.G., et al. (2018). Pattern and process in hominin brain size "
   "evolution are scale-dependent. <em>Proceedings of the Royal Society B</em> 285(1873), 20172738.",
   "10.1098/rspb.2017.2738",
   "Conclusions about when and how fast brains grew depend substantially on how the data are binned."),
 "pearce2013": ("Pearce, E., Stringer, C. &amp; Dunbar, R.I.M. (2013). New insights into differences in "
   "brain organization between Neanderthals and anatomically modern humans. "
   "<em>Proceedings of the Royal Society B</em> 280(1758), 20130168.", "10.1098/rspb.2013.0168",
   "Argues more of the larger Neanderthal brain was given over to vision and body control, so equal "
   "volume need not mean equal general cognition."),
 "monson2026": ("Monson, T.A., Weitz, A.P. &amp; Brasil, M.F. (2026). The evolution of brain and body "
   "size in genus <em>Homo</em>. <em>Humans</em> 6(2), 12.", "10.3390/humans6020012",
   "Finds <em>Homo</em> brain-body scaling positively allometric and distinct from the wider primate "
   "slope, with <em>H. floresiensis</em> and <em>H. naledi</em> falling where their body size predicts."),
}


LIT.update({
 "roberts1953": ("Roberts, D.F. (1953). Body weight, race and climate. <em>American Journal of "
   "Physical Anthropology</em> 11(4), 533&ndash;558.", "10.1002/ajpa.1330110404",
   "The original demonstration that human body weight tracks mean annual temperature across "
   "populations. Every later treatment of Bergmann's rule in humans measures itself against this."),
 "riemer2018": ("Riemer, K., Guralnick, R.P. &amp; White, E.P. (2018). No general relationship "
   "between mass and temperature in endothermic species. <em>eLife</em> 7, e27166.",
   "10.7554/eLife.27166",
   "Across a large sample of birds and mammals, no consistent mass-temperature relationship. A "
   "direct challenge to Bergmann's rule as a general law rather than a local pattern."),
 "willstock2016": ("Will, M. &amp; Stock, J.T. (2015). Spatial and temporal variation of body size "
   "among early <em>Homo</em>. <em>Journal of Human Evolution</em> 82, 15&ndash;33.",
   "10.1016/j.jhevol.2015.02.009",
   "Across 39 postcranial specimens, no simple geographic or chronological trend in early "
   "<em>Homo</em> body size."),
 "balcarcel2021": ("Balcarcel, A.M., Veitschegger, K., Clauss, M. &amp; Sánchez-Villagra, M.R. "
   "(2021). Intensive human contact correlates with smaller brains: differential brain size "
   "reduction in cattle types. <em>Proceedings of the Royal Society B</em> 288(1952), 20210813.",
   "10.1098/rspb.2021.0813",
   "Brain size reduction under domestication scales with the intensity of human contact rather "
   "than with domestication as a binary state."),
 "johnsson2021": ("Johnsson, M., Henriksen, R. &amp; Wright, D. (2021). The neural crest cell "
   "hypothesis: no unified explanation for domestication. <em>Genetics</em> 219(1), iyab097.",
   "10.1093/genetics/iyab097",
   "Argues the neural crest hypothesis does not provide a unified explanation for the "
   "domestication syndrome. Wilkins, Wrangham and Fitch published a reply in the same issue."),
 "wilkins2021reply": ("Wilkins, A.S., Wrangham, R.W. &amp; Fitch, W.T. (2021). The neural crest/domestication "
   "syndrome hypothesis, explained: reply to Johnsson, Henriksen, and Wright. <em>Genetics</em> "
   "219(1), iyab098.", "10.1093/genetics/iyab098",
   "The authors' response defending the neural crest account against Johnsson and colleagues."),
 "lord2020": ("Lord, K.A., Larson, G., Coppinger, R.P. &amp; Karlsson, E.K. (2020). The history of "
   "farm foxes undermines the animal domestication syndrome. <em>Trends in Ecology &amp; "
   "Evolution</em> 35(2), 125&ndash;136.", "10.1016/j.tree.2019.10.011",
   "The Russian farm-fox experiment used founders already bred in captivity for decades, which "
   "undercuts its standing as a clean demonstration of the domestication syndrome."),
 "gleeson2023": ("Gleeson, B.T. &amp; Wilson, L.A.B. (2023). Shared reproductive disruption, not "
   "neural crest or tameness, explains the domestication syndrome. <em>Proceedings of the Royal "
   "Society B</em> 290(1995), 20222464.", "10.1098/rspb.2022.2464",
   "A third mechanism for the domestication syndrome, independent of both neural crest deficits "
   "and selection on tameness."),
})


LIT.update({
 "puschel2024": ("Püschel, T.A., Nicholson, S.L., Baker, J., Barton, R.A. &amp; Venditti, C. (2024). "
   "Hominin brain size increase has emerged from within-species encephalization. "
   "<em>PNAS</em> 121(49), e2409542121.", "10.1073/pnas.2409542121",
   "Across 285 specimens and 1,000 Bayesian phylogenies, finds a significant within-species time "
   "effect on relative brain size and no significant between-species effect. Encephalization "
   "accumulated inside lineages rather than through species turnover."),
 "gingerich2022": ("Gingerich, P.D. (2022). Pattern and rate in the Plio-Pleistocene evolution of "
   "modern human brain size. <em>Scientific Reports</em> 12(1), 11216.", "10.1038/s41598-022-15481-3",
   "Synthesises 14 studies into one endocranial series and finds four phases: stasis, increase, "
   "stasis, increase. Argues tempo and mode are both scale-dependent."),
 "willpablos2017": ("Will, M., Pablos, A. &amp; Stock, J.T. (2017). Long-term patterns of body mass "
   "and stature evolution within the hominin lineage. <em>Royal Society Open Science</em> 4(11), "
   "171339.", "10.1098/rsos.171339",
   "254 body mass and 204 stature estimates across 311 specimens from 4.4 Ma. The main study "
   "testing Cope's rule against the hominin record."),
 "gardner2026": ("Gardner, J.D., Püschel, T.A., White, S., Sakamoto, M. &amp; Venditti, C. (2026). "
   "Competing models of hominin body size evolution. <em>PNAS</em> 123(27), e2521732123.",
   "10.1073/pnas.2521732123",
   "386 specimens across 21 taxa. Finds marked body mass increase in later Homo and moderate "
   "support for a general increase. A correction was issued in August 2026 (doi:10.1073/pnas.2625195123)."),
 "montgomery2010": ("Montgomery, S.H., Capellini, I., Barton, R.A. &amp; Mundy, N.I. (2010). "
   "Reconstructing the ups and downs of primate brain evolution. <em>BMC Biology</em> 8, 9.",
   "10.1186/1741-7007-8-9",
   "Explicitly tests Cope's rule across primates and rejects it. Brain size is treated separately "
   "from body size throughout."),
})


def lit(key, note=False):
    """Render a wider-literature citation."""
    c, doi, n = LIT[key]
    out = c
    if doi:
        out += f' <a href="https://doi.org/{doi}">doi:{doi}</a>'
    if note:
        out += f" {n}"
    return out


PARTICLES = {"de", "del", "della", "van", "von", "der", "la", "le", "di", "da", "dos"}


def _surname_initials(full):
    """'Jeff Morgan Stibel' -> 'Stibel, J.M.'  'Liberato De Caro' -> 'De Caro, L.'"""
    parts = full.replace("&nbsp;", " ").split()
    # walk back from the end collecting the surname, absorbing particles
    i = len(parts) - 1
    while i > 0 and parts[i - 1].lower().rstrip(".") in PARTICLES:
        i -= 1
    surname = " ".join(parts[i:])
    given = parts[:i]
    inits = "".join(g[0].upper() + "." for g in given if g)
    return f"{surname}, {inits}" if inits else surname


def _authors_short(authors):
    names = [_surname_initials(a) for a in authors]
    if len(names) == 1:
        return names[0]
    if len(names) <= 3:
        return ", ".join(names[:-1]) + " &amp; " + names[-1]
    return names[0] + " et al."


def _surname(full):
    parts = full.split()
    i = len(parts) - 1
    while i > 0 and parts[i - 1].lower().rstrip(".") in PARTICLES:
        i -= 1
    return " ".join(parts[i:])


# Same first author + same year => bibliographic letter suffix.
# Ordered by publication date, not slug: the BBE climate paper appeared first.
YEAR_SUFFIX = {"stibel2023climate": "a", "stibel2023body": "b"}


def _check_suffixes():
    """Fail loudly if a new author-year collision appears without a letter."""
    from collections import defaultdict
    g = defaultdict(list)
    for k, v in PAPERS.items():
        g[(_surname(v["authors"][0]).lower(), v["year"])].append(k)
    missing = [k for keys in g.values() if len(keys) > 1 for k in keys
               if k not in YEAR_SUFFIX]
    if missing:
        raise ValueError("author-year collision needs a YEAR_SUFFIX entry: %s" % missing)


def yr(key):
    """Year with its disambiguating letter, e.g. '2023a'."""
    return "%d%s" % (PAPERS[key]["year"], YEAR_SUFFIX.get(key, ""))


def _sortkey(key):
    """Alphabetical by first author surname, then year."""
    if key in PAPERS:
        p = PAPERS[key]
        return (_surname(p["authors"][0]).lower(), int(p["year"]), YEAR_SUFFIX.get(key, ""))
    c = re.sub(r"<[^>]+>", "", LIT[key][0])
    sur = c.split(",")[0].strip().lower()
    m = re.search(r"\((\d{4})\)", c)
    return (sur, int(m.group(1)) if m else 0, "")


def sources(keys, pre="", note=False):
    """Render a de-duplicated, alphabetised source list."""
    seen, uniq = set(), []
    for k in keys:
        if k not in seen:
            seen.add(k); uniq.append(k)
    items = "".join(
        "<li>%s</li>" % (src(k, pre) if k in PAPERS else lit(k, note))
        for k in sorted(uniq, key=_sortkey))
    return '<ul class="lit">%s</ul>' % items


def src(key, pre=""):
    """Render a PAPERS entry for an on-page source list, linked to its own page."""
    p = PAPERS[key]
    out = f'{_authors_short(p["authors"])} ({yr(key)}). '
    out += f'<a href="{pre}papers/{p["slug"]}.html">{p["title"]}</a>.'
    if p.get("journal"):
        j = f' <em>{p["journal"]}</em>'
        if p.get("volume"):
            j += f' {p["volume"]}'
            if p.get("issue"):
                j += f'({p["issue"]})'
        if p.get("pages"):
            j += f', {p["pages"]}'
        out += j + "."
    if p.get("doi"):
        out += f' <a href="https://doi.org/{p["doi"]}">doi:{p["doi"]}</a>'
    return out


_check_suffixes()
