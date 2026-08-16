# -*- coding: utf-8 -*-
"""Page content for the reference hub. Run this file to build the site."""
import os, json, html
from papers import PAPERS, CORE_FIVE, CONTEXT_PAPERS, citation
from build import (shell, write, paper_card, lic_pill, scholarly_ld,
                   article_ld, faq_ld, OUT, NAV, BASE, SITE_NAME)

P = PAPERS

# =========================================================== 1. OVERVIEW
def page_index():
    d = ("Human brain size appears to have declined since the Late Pleistocene, but the timing "
         "and cause are actively disputed among researchers. A sourced summary of the evidence "
         "on both sides.")
    body = f"""
<h1>Has the human brain gotten smaller?</h1>

<div class="answer">
<p><strong>Probably yes — but the timing is genuinely disputed, and the reason is unresolved.</strong>
Nineteen studies published over roughly ninety years report a decrease in human cranial capacity
since the Pleistocene, averaging 8.5%. A 2022 reanalysis of the underlying data found no detectable
decline and remains the standing counter-analysis. The disagreement is methodological — about
dataset comparability and the modern reference value — not ideological.</p>
</div>

<p class="upd">Reviewed 15 August 2026 &middot; 11 primary sources &middot; both positions represented</p>

<h2>What is broadly agreed</h2>
<ul>
<li><strong>Brain size grew dramatically across most of the genus <em>Homo</em>.</strong> This is one of the
best-documented trends in human evolution and is not disputed by anyone in this exchange.</li>
<li><strong>Pleistocene <em>H. sapiens</em> and Würm-period Neanderthals had comparably large brains</strong>
— about 1,458 cc and 1,459 cc respectively
(<a href="papers/{P['desilva2023']['slug']}.html">DeSilva et al. 2023</a>).</li>
</ul>

<h2>What is disputed</h2>
<ul>
<li><strong>The modern human average.</strong> Estimates range from about 1,297 cc to 1,460 cc depending on
the reference dataset. This is not a detail — if the modern anchor is set too low, an apparent decline
follows arithmetically. It is
<a href="papers/{P['villmoare2022']['slug']}.html">Villmoare &amp; Grabowski's</a> central objection.</li>
<li><strong>Whether a Holocene reduction is statistically detectable at all</strong>, and if so, when.</li>
<li><strong>Whether brain growth stopped ~300,000 years ago.</strong> One recent analysis of 800 cranial
measurements finds no significant growth trend after that point
(<a href="papers/{P['stibel2025']['slug']}.html">Stibel 2025</a>). This has not yet been independently
replicated.</li>
</ul>

<h3>The four positions</h3>
<table>
<tr><th>Position</th><th>Core claim</th><th>Principal source</th></tr>
<tr><td>Reduction occurred, recently</td>
<td>A significant decline occurred in the Holocene, possibly within the last 5,000–3,000 years</td>
<td><a href="papers/{P['desilva2021']['slug']}.html">DeSilva et al. 2021</a>;
<a href="papers/{P['desilva2023']['slug']}.html">2023</a></td></tr>
<tr><td>No reduction detectable</td>
<td>Reanalysis of the same data detects no reduction over any period since ~300,000 years ago</td>
<td><a href="papers/{P['villmoare2022']['slug']}.html">Villmoare &amp; Grabowski 2022</a></td></tr>
<tr><td>Reduction is largely allometric</td>
<td>Brain decline tracks body decline; controlled for lean body mass, the change is isometric</td>
<td><a href="papers/{P['stibel2021']['slug']}.html">Stibel 2021</a></td></tr>
<tr><td>Reduction is environmentally driven</td>
<td>Brain and body size both track temperature; warming periods correlate with smaller size</td>
<td><a href="papers/{P['stibel2023climate']['slug']}.html">Stibel 2023a</a>;
<a href="papers/{P['stibel2023body']['slug']}.html">2023b</a></td></tr>
</table>

<p>The full exchange — four published rounds between 2021 and 2024 — is set out on
<a href="the-debate.html">the debate page</a>. It is the single most misreported part of this
topic: most coverage stops at the 2022 rebuttal and never reports the 2023 response.</p>

<h2>The proposed explanations</h2>
<p><em>If</em> a reduction occurred — which Villmoare &amp; Grabowski dispute — four mechanisms have been
argued for it. None is established, and they are not mutually exclusive.</p>

<div class="card"><h3>1. Body size</h3>
<p>Brains scale with bodies. If bodies got smaller, brains would follow without any change in
cognitive selection. Controlling for <em>lean</em> body mass, one analysis finds the change isometric —
implying much of the measured decline in encephalization reflects modern obesity inflating the
body-mass denominator rather than neural loss.
<a href="cognition.html">More &rarr;</a></p></div>

<div class="card"><h3>2. Climate</h3>
<p>Across 298 specimens and 50,000 years, brain size averages roughly 10.7% lower in warmer periods.
The same pattern appears in body mass across 700,000 years. Thermoregulation offers a plausible
mechanism. But the paper says climate itself accounts for only a small share of variation; models
reach ~40% only after adding sex and latitude as covariates.
<a href="climate.html">More &rarr;</a></p></div>

<div class="card"><h3>3. Metabolic ceiling</h3>
<p>Brains consume roughly 20% of adult resting energy and up to 60% in early development. Beyond some
size, the cost may outweigh the benefit — turning directional selection into stabilizing selection.
<a href="papers/{P['stibel2025']['slug']}.html">More &rarr;</a></p></div>

<div class="card"><h3>4. Cognitive offloading</h3>
<p>If information can be stored outside the head — in symbols, tools, writing, other people — the
selective advantage of carrying more neural tissue weakens. The chronology of symbolic artefacts
overlaps the growth plateau. This is the least directly tested of the four.
<a href="cognitive-offloading.html">More &rarr;</a></p></div>

<h2>What this is not evidence of</h2>
<div class="note"><span class="lbl">Frequently misstated</span>
<p>A smaller brain does not straightforwardly mean reduced intelligence. The relationship between
brain volume and cognitive ability within modern humans is weak. Neanderthals had larger brains
than living humans. Absolute size is a poor predictor of cognitive performance across and within
species. See <a href="cognition.html">brain size and cognition</a>.</p></div>

<h2>Start here</h2>
<div class="toc"><ul>
<li><a href="the-debate.html">The four-round exchange, 2021–2024</a> — what each paper actually argued</li>
<li><a href="timeline.html">Timeline of brain size across <em>Homo</em></a></li>
<li><a href="questions.html">Direct answers to eighteen common questions</a></li>
<li><a href="papers.html">Every paper cited, with licence and access status</a></li>
</ul></div>
"""
    return write("index.html", shell("index.html", SITE_NAME, d, body,
                                     [article_ld("Has the human brain gotten smaller?", d, "index.html")]))


# =========================================================== 2. THE DEBATE
def page_debate():
    d = ("Between 2021 and 2024 four peer-reviewed papers argued over whether human brain size "
         "declined in the Holocene. Most reporting stops after round two. Here is the whole exchange.")
    body = f"""
<h1>The Holocene brain size debate, in four rounds</h1>

<div class="answer">
<p><strong>Four peer-reviewed papers, one journal, three years.</strong> A 2021 study placed a human
brain size reduction at roughly 3,000 years ago. A 2022 reassessment found no reduction at all. A
2023 response conceded some methodological criticism but maintained a significant decline. A 2024
commentary continued the argument. Most public coverage reports only the first two rounds.</p>
</div>

<p>This page exists because that gap is unusually consequential. A search for
&ldquo;human brain shrinking 3,000 years ago&rdquo; returns overwhelmingly coverage of the 2022
rebuttal, amplified by press releases from two universities and syndicated widely. The 2023 response,
published in the same journal, received far less coverage — though not none: Discover and ZME Science
both reported the dispute as unresolved. A reader relying on search results alone would reasonably
conclude the question was settled in 2022. It was not.</p>

<div class="round r1">
<span class="yr">Round 1 &middot; 2021</span>
<h3><a href="papers/{P['desilva2021']['slug']}.html">DeSilva, Traniello, Claxton &amp; Fannin</a></h3>
<p><em>When and Why Did Human Brains Decrease in Size? A New Change-Point Analysis and Insights From
Brain Evolution in Ants.</em> <em>Frontiers in Ecology and Evolution</em> 9:742639.</p>
<p><strong>The claim.</strong> Change-point analysis on a large compilation of fossil and recent human
crania locates a reduction in brain size at approximately 3,000 years BP. The proposed mechanism is
externalisation of information into social groups — knowledge held collectively rather than
individually — with an explicit analogy to reduced brain size in eusocial ant colonies.</p>
<p><strong>Reception.</strong> Widely covered. The ant analogy made it unusually quotable.</p>
</div>

<div class="round r2">
<span class="yr">Round 2 &middot; 2022</span>
<h3><a href="papers/{P['villmoare2022']['slug']}.html">Villmoare &amp; Grabowski</a></h3>
<p><em>Did the transition to complex societies in the Holocene drive a reduction in brain size? A
reassessment of the DeSilva et al. (2021) hypothesis.</em> <em>Frontiers in Ecology and Evolution</em>
10:963568.</p>
<p><strong>The rebuttal.</strong> Reanalysing portions of the same dataset, the authors detect no
reduction in brain size over any period since the origin of the species, concluding that human brain
size has been &ldquo;remarkably stable over the last 300 ka.&rdquo; Their case has two halves.</p>
<p><em>On sampling:</em></p>
<ul>
<li>The dataset pools specimens from radically different populations and geographies — England,
China, Mali, Algeria — as though directly comparable.</li>
<li>Only <strong>23 crania</strong> fall inside the time window critical to the hypothesis.</li>
<li><strong>578 of the roughly 987 specimens</strong> represent only the last 100 years of a span
covering some 9.8 million years, biasing the change-point estimate toward the recent.</li>
</ul>
<p><em>On the statistics — the more forceful half, and the part usually left out of summaries:</em></p>
<ul>
<li><strong>The modern reference value may be wrong.</strong> The original dataset generates a modern
human mean of about <strong>1,297 cc</strong>, well below other published estimates ranging from
~1,340 cc to ~1,460 cc. If the modern anchor is set too low, a decline follows arithmetically whether
or not one occurred. This is their central substantive objection.</li>
<li><strong>The change point was never tested for significance.</strong> Applying a Davies (1987) test,
Villmoare &amp; Grabowski find <strong>no significant change point</strong> near 3 ka —
<em>p</em> = 0.621 on the full data, 0.739 restricted to 300 ka, 0.259 restricted to 30 ka — and
document violated regression assumptions in the original analysis.</li>
</ul>
<p>DeSilva et al. (2023) devote a section of their response, &ldquo;How big is the average human
brain?&rdquo;, specifically to the modern-mean objection.</p>
<p><strong>Reception.</strong> Amplified by press releases from the University of Nevada, Las Vegas and
Liverpool John Moores University, then syndicated through ScienceDaily, Advanced Science News,
Neuroscience News, Technology Networks, Gulf News, Haaretz, Discover and others.</p>
</div>

<div class="round r3">
<span class="yr">Round 3 &middot; 2023</span>
<h3><a href="papers/{P['desilva2023']['slug']}.html">DeSilva, Fannin, Cheney, Claxton, Ilieş, Kittelberger, Stibel &amp; Traniello</a></h3>
<p><em>Human brains have shrunk: the questions are when and why.</em> <em>Frontiers in Ecology and
Evolution</em> 11:1191274.</p>
<p><strong>The response.</strong> The authors concede real ground and hold the central claim:</p>
<ul>
<li><strong>Conceded:</strong> the Holocene portion of the original dataset is skewed toward modern
specimens — an unavoidable taphonomic bias that may pull the change-point estimate too recent and
could obscure earlier change points.</li>
<li><strong>Conceded:</strong> errata. Four juvenile Neanderthal specimens and one duplicate entry were
removed. The Morton Collection was removed as a dataset that &ldquo;has been used to promote false
and dangerous ideas of white supremacy.&rdquo; Removing it did not appreciably change the result.</li>
<li><strong>Maintained:</strong> across 19 published studies spanning about 90 years — several by the
same research groups — the average reported decrease is <strong>8.5%</strong>. The Pleistocene–Holocene difference remains
significant (Welch's <em>t</em> = 9.15, <em>p</em> &lt; 0.0001), and holds across three separate modern
reference datasets totalling nearly 9,000 individuals.</li>
<li><strong>Reframed:</strong> the title concedes the timing question. The authors' position becomes
that a reduction happened, that its date is uncertain across roughly 5,000–3,000 BP, and that
colleagues should keep investigating.</li>
</ul>
<p><strong>Reception.</strong> Substantially less coverage than round 2, and it is the round most often
missing from public accounts of the dispute.</p>
</div>

<div class="round r4">
<span class="yr">Round 4 &middot; 2024</span>
<h3><a href="papers/{P['decaro2024']['slug']}.html">De Caro</a></h3>
<p><em>Commentary: Human brains have shrunk: the questions are when and why.</em> <em>Frontiers in
Ecology and Evolution</em>, 11 April 2024.</p>
<p>A published commentary continuing the exchange — evidence that the question remained open in the
literature well after the press cycle concluded.</p>
</div>

<h2>Where that leaves the question</h2>
<p>Honestly: unresolved, and narrower than it looks.</p>
<ul>
<li><strong>Neither analysis has been superseded.</strong> Villmoare &amp; Grabowski remains the standing
counter-analysis; the 2023 response remains the standing reply.</li>
<li><strong>The disagreement is largely methodological</strong> — about whether crania from different
populations and periods can be pooled, and how much a modern-skewed sample distorts a change-point
estimate. These are legitimate technical disputes, not opposed worldviews.</li>
<li><strong>The observation predates the dispute.</strong> <a href="papers/{P['henneberg1988']['slug']}.html">Henneberg
(1988)</a> reported decreasing Holocene skull size, and
<a href="papers/{P['hawks2011']['slug']}.html">Hawks (2011)</a> argued for selection toward smaller brains
— both cited by both sides.</li>
<li><strong>Independent teams get partly convergent results.</strong>
<a href="papers/{P['will2021']['slug']}.html">Will et al. (2021)</a>, working separately, found climate a
strong predictor of body size in <em>Homo</em> but only a weak, indirect predictor of brain size.</li>
</ul>

<div class="note"><span class="lbl">If you take one thing from this page</span>
<p>The accurate summary is not &ldquo;human brains shrank&rdquo; and not &ldquo;that was
debunked.&rdquo; It is: <strong>a decrease is reported in nineteen studies over ninety years and is
disputed on methodological grounds — the modern reference value, dataset comparability, and whether
the change point is statistically significant — by a 2022 reanalysis that its original authors
answered in 2023. The timing is uncertain and the cause is unresolved.</strong></p></div>
"""
    return write("the-debate.html",
                 shell("the-debate.html", "The Holocene brain size debate", d, body,
                       [article_ld("The Holocene brain size debate, in four rounds", d, "the-debate.html")]))


# =========================================================== 3. TIMELINE
def page_timeline():
    d = ("A chronology of brain size across the genus Homo, from early expansion through the "
         "plateau around 300,000 years ago to the disputed Holocene decline.")
    body = f"""
<h1>Timeline of brain size in <em>Homo</em></h1>

<div class="answer">
<p><strong>Brain size in <em>Homo</em> roughly tripled, then stopped.</strong> Expansion dominates the
Early and Middle Pleistocene. Growth flattens around 300,000 years ago. Late Pleistocene humans and
Neanderthals converge near 1,460 cc. Modern averages sit near 1,300–1,350 cc — a gap whose
interpretation is the subject of the current dispute.</p>
</div>

<table>
<tr><th>Period</th><th>What the record shows</th><th>Source</th></tr>
<tr><td>~2.0 and ~1.5 Ma</td>
<td>Statistically significant shifts in the <em>rate</em> of hominin endocranial volume change
(95% CI 2.0–2.3 Ma and 1.2–1.8 Ma)</td>
<td>DeSilva et al. 2023</td></tr>
<tr><td>Early Pleistocene</td>
<td>Strong directional growth in brain size across the genus</td>
<td>Stibel 2025</td></tr>
<tr><td><strong>~300,000 BP</strong></td>
<td><strong>Growth plateaus.</strong> No significant trend in brain size growth after this point across
800 cranial measurements</td>
<td>Stibel 2025</td></tr>
<tr><td>300–100 kyr BP</td>
<td>No significant difference between glacial and interglacial populations (<em>p</em> = 0.923)</td>
<td>Stibel 2025</td></tr>
<tr><td>~142–75 kyr BP</td>
<td>First symbolic artefacts: Bizmoune Cave shell beads, Blombos Cave engraved ochre</td>
<td>Stibel 2025</td></tr>
<tr><td>100–0 kyr BP</td>
<td>Glacial–interglacial differences in brain size emerge for the first time (<em>p</em> &lt; 0.0001)</td>
<td>Stibel 2025</td></tr>
<tr><td>300–11.7 kyr BP</td>
<td>Pleistocene <em>H. sapiens</em> average <strong>1,458 ± 140 cc</strong> (n = 136). Würm-period
Neanderthals (&lt;115 kyr BP) average <strong>1,459 ± 182 cc</strong> (n = 14)</td>
<td>DeSilva et al. 2023</td></tr>
<tr><td>~50 kyr BP onward</td>
<td>Brain mass declines <strong>5.4%</strong> relative to the Upper Palaeolithic; body mass declines in
parallel</td>
<td>Stibel 2021</td></tr>
<tr><td>~15 kyr BP</td>
<td>Climate-linked size response appears to begin, and may persist to the present</td>
<td>Stibel 2023a</td></tr>
<tr><td>Holocene (12 kyr BP–now, per this study)</td>
<td>Mean <strong>1,281.95 ± 141.58 g</strong> (n = 235) versus Pleistocene 1,426.96 ± 139.28 g (n = 63)</td>
<td>Stibel 2023a</td></tr>
<tr><td><strong>5,000–3,000 BP</strong></td>
<td><strong>Disputed.</strong> The window in which a reduction is argued to have occurred — and in which a
reanalysis finds none</td>
<td>DeSilva 2021/2023; Villmoare &amp; Grabowski 2022</td></tr>
<tr><td>Last 1,000 years</td>
<td>Encephalization trend reverses sign (<em>r</em> = −0.483) against a positive prehistoric trend
(<em>r</em> = 0.777)</td>
<td>Stibel 2021</td></tr>
<tr><td>Present</td>
<td>Modern estimates range 1,308–1,392 cc, weighted average <strong>1,345 cc</strong> (n = 8,961)</td>
<td>DeSilva et al. 2023</td></tr>
</table>

<div class="note"><span class="lbl">Reading this table carefully</span>
<p>Different rows use different units. Cranial capacity in cubic centimetres and brain mass in grams
are related but not interchangeable. Stibel (2021, 2023, 2025) converts using Ruff et al.'s equation,
brain mass = 1.147 &times; (cranial capacity)<sup>0.976</sup>; DeSilva et al. (2023) average two published
equations instead. Comparisons across rows drawn from different studies are indicative, not precise.</p></div>

<h2>The shape of the curve matters more than any single number</h2>
<p>The two halves of this timeline are contested very differently. Expansion through the Pleistocene
is well established and uncontroversial. The plateau at ~300,000 BP is a recent finding from a large
single-analysis dataset. The Holocene decline is the only part under active dispute — and it is the
part that receives essentially all public attention.</p>
"""
    return write("timeline.html", shell("timeline.html", "Timeline of brain size in Homo", d, body,
                                        [article_ld("Timeline of brain size in Homo", d, "timeline.html")]))


# =========================================================== 4. CLIMATE
def page_climate():
    d = ("Studies across 298 specimens and 50,000 years find human brain size averaging about 10.7% "
         "lower in warmer climate periods, with body mass showing a parallel pattern over 700,000 years.")
    body = f"""
<h1>Climate and human brain size</h1>

<div class="answer">
<p><strong>Warmer periods correlate with smaller brains and smaller bodies.</strong> Across 298
<em>Homo</em> specimens over 50,000 years, brain size averages roughly <strong>10.7% lower</strong>
during warming periods than cooler ones. Body mass shows the same direction across 700,000 years.
The relationship is correlational, and climate accounts for only about 40% of the variation.</p>
</div>

<h2>The brain size finding</h2>
<p><a href="papers/{P['stibel2023climate']['slug']}.html">Stibel (2023)</a> tested temperature, humidity
and precipitation against cranial capacity in 298 specimens, using 373 independent measurements and
multiple paleoclimate records.</p>
<ul>
<li>Inverse relationship with temperature: <em>r</em> = −0.362, <em>p</em> &lt; 0.0001, holding after
controls for geography, sex and taxon.</li>
<li>Cooler periods: <strong>1,426.31 g ± 137.30</strong> (n = 65). Warmer: <strong>1,280.89 g ± 141.67</strong>
(n = 233). A difference of about <strong>10.74%</strong>.</li>
<li>By epoch: Pleistocene 1,426.96 g versus Holocene 1,281.95 g — a 10.71% difference.</li>
<li>Restricted to anatomically modern <em>Homo</em>, the gap is 11.02%.</li>
<li>The spatiotemporal signal appears to begin roughly 15,000 years ago.</li>
<li>Humidity is a weaker predictor (5.28%, <em>p</em> &lt; 0.002); precipitation is not significant
(2.74%, <em>p</em> = 0.061).</li>
</ul>

<h2>The body size finding</h2>
<p><a href="papers/{P['stibel2023body']['slug']}.html">Stibel (2023)</a> ran the parallel analysis on body
mass and shape across 247 specimens and 700,000 years, against five independent paleoclimate records.</p>
<ul>
<li>Cooler periods: <strong>66.40 kg ± 0.86</strong>. Warmer: <strong>59.00 kg ± 0.73</strong> — an
<strong>11.8%</strong> difference.</li>
<li>The model accounts for roughly <strong>half</strong> of total body mass variation
(<em>r</em>² = 0.51).</li>
<li>Body <em>shape</em> shifts too: stature-to-mass ratio is 7.09% greater in warmer cycles, consistent
with more linear builds in heat.</li>
<li><strong>Stature alone shows no significant difference</strong> (<em>p</em> = 0.07). Climate tracks
mass and proportion, not height.</li>
<li>The pattern replicates across independent records: Lake Malawi 12.53%, North Atlantic deep-sea
11.04%, African fossils only 13.59%.</li>
</ul>

<h2>Why this is a plausible mechanism</h2>
<p>Thermoregulation. Larger bodies conserve heat better in cold and shed it worse in heat — the
principle behind Bergmann's and Allen's rules, observed across many endothermic species. Brains are
metabolically expensive and thermally costly. If bodies track temperature and brains track bodies,
brain size would follow climate without requiring any change in selection on cognition itself.</p>

<h2>What the studies do not establish</h2>
<div class="note"><span class="lbl">Stated limitations</span>
<p>The climate paper states its data &ldquo;can only provide correlational support for spatiotemporal
relationships.&rdquo; Causal direction is explicitly unresolved: the author notes it is unclear whether
brain size was selected on directly or drifted alongside body size. Sampling is biased toward
high-latitude specimens (220 of 298) and males (167 of 257 sexed). Effects vanish at temperature
extremes (<em>p</em> &gt; 0.50), appearing only across moderate ranges. And climate accounts for only a
minority of total variation — the paper says brain size adaptations &ldquo;are likely driven by other
factors.&rdquo;</p></div>

<h2>An independent team, partly different answer</h2>
<p><a href="papers/{P['will2021']['slug']}.html">Will et al. (2021)</a>, in <em>Nature Communications</em>,
examined environmental predictors of body and brain size in <em>Homo</em> over a million years. They
found temperature a strong predictor of <strong>body</strong> size — converging with the finding above —
but concluded that <strong>brain</strong> size was better predicted by non-climatic factors. Any account
of this literature that cites only one of these two results is incomplete.</p>

<h2>Does this mean current warming is shrinking our brains?</h2>
<p>No such claim is established. The climate paper notes the adaptive response &ldquo;may persist into
modern times,&rdquo; which is a hypothesis about a multi-millennial evolutionary signal, not a
prediction about individuals alive today. Evolutionary responses of this kind operate across
hundreds of generations. Several news outlets have compressed this into headlines about climate
change shrinking human brains; that framing outruns the evidence.</p>
"""
    return write("climate.html", shell("climate.html", "Climate and human brain size", d, body,
                                       [article_ld("Climate and human brain size", d, "climate.html")]))


# =========================================================== 5. BODY SIZE
def page_body():
    d = ("Human body mass and body proportions track climate across 700,000 years. Because brains "
         "scale with bodies, body size change is a leading candidate explanation for brain size change.")
    body = f"""
<h1>Body size, proportion, and what it explains</h1>

<div class="answer">
<p><strong>Bodies got smaller too — and brains scale with bodies.</strong> Across 247 <em>Homo</em>
specimens and 700,000 years, body mass averages <strong>11.8% lower</strong> in warmer periods. Body
shape shifts as well. This matters because a brain that shrinks in proportion to its body is not
evidence of cognitive change; it is allometry.</p>
</div>

<h2>Why body size is the first thing to check</h2>
<p>Across mammals, brain mass scales predictably with body mass. Any claim that human brains got
smaller in a way that <em>means</em> something must first rule out the possibility that brains simply
tracked shrinking bodies. This is the question
<a href="papers/{P['stibel2021']['slug']}.html">Stibel (2021)</a> was built to test — and the answer
substantially complicates the simple narrative.</p>

<h3>The isometry result</h3>
<p>Using matched body remains to compute encephalization across an evolutionary timespan, the paper
finds modern humans <strong>17% less encephalized</strong> than the <em>H. sapiens</em> comparison sample.
But controlled for <strong>lean</strong> body mass, the change becomes <strong>isometric</strong> — meaning
brain and body changed in proportion.</p>
<p>The implication is counterintuitive and worth stating plainly: much of the apparent decline in
modern encephalization may be an artefact of <strong>modern obesity</strong> inflating the body-mass
denominator, rather than a loss of neural tissue. The modern sample's mean BMI is 25.3, in the
overweight range, and BMI correlates with encephalization quotient at <em>r</em> = 0.84 in that sample.</p>
<p>Supporting this, the brain–body relationship that holds tightly across earlier hominins
(<em>r</em> = 0.66–0.82) <strong>breaks down entirely</strong> in the modern sample (<em>r</em> = 0.08,
<em>p</em> = 0.75) — the signature of a denominator that has been disturbed by something other than
evolution.</p>

<div class="note"><span class="lbl">Sample caution</span>
<p>The modern comparison rests on autopsy data from <strong>19 individuals</strong> — 11 German and 8
Australian Aboriginal males, all deceased 1980–82. That is a small and geographically narrow basis
for a claim about modern humans generally, and it is a real limit on how far the isometry result can
be pushed.</p></div>

<h2>Body shape, not just size</h2>
<p><a href="papers/{P['stibel2023body']['slug']}.html">Stibel (2023)</a> extends this to proportionality
across 87 specimens:</p>
<ul>
<li>Stature-to-body-mass ratio is <strong>7.09% greater</strong> in warmer cycles (9.89% at 10,000-year
averaging) — more linear builds in heat, stockier builds in cold.</li>
<li><strong>Stature itself does not significantly differ</strong> across temperature cycles
(<em>p</em> = 0.07). Climate acts on mass and proportion, not height.</li>
<li>The author flags a taxonomic implication: because morphology is used to classify within
<em>Homo</em>, some species boundaries may partly reflect climatic period rather than phylogeny.</li>
</ul>
<p>The paper is candid that this section is its weakest. The sample is small and skewed
high-latitude (82 of 87) and male. Testing proportionality is &ldquo;approximate at best.&rdquo; Results
using the Ponderal Index were <strong>not</strong> significant, and the author notes the shape effect may
simply be an artefact of the strong body-mass effect.</p>

<h2>Where this leaves the brain question</h2>
<p>Body size change does not dissolve the brain size question, but it constrains it. If a substantial
share of measured brain decline is allometric — brains tracking bodies — then the residual requiring
a cognitive or cultural explanation is smaller than headline figures suggest. Combined with the
observation that climate models account for only about 40–50% of variation, a large fraction of the
variance in human brain size remains unexplained by any published mechanism.</p>
<p>That unexplained remainder is what motivates the
<a href="cognitive-offloading.html">cognitive offloading</a> hypothesis.</p>
"""
    return write("body-size.html", shell("body-size.html", "Body size and proportionality", d, body,
                                         [article_ld("Body size, proportion, and what it explains", d, "body-size.html")]))


# =========================================================== 6. COGNITION
def page_cognition():
    d = ("Does a smaller brain mean lower intelligence? The relationship between brain size and "
         "cognitive ability is weak, and researchers in this literature describe it as spurious at best.")
    body = f"""
<h1>Brain size and cognitive ability</h1>

<div class="answer">
<p><strong>Brain size is a poor predictor of intelligence.</strong> Within modern humans the
correlation between brain volume and cognitive test performance is weak. Neanderthals had larger
brains than living humans. Measured cognitive performance has risen over the same century in which
brain size is argued to have fallen. Size, organisation and efficiency are different things.</p>
</div>

<h2>The claim researchers actually make</h2>
<p>This is the most misreported area of the topic, and it is also the place where a single sentence
from the literature is most often quoted at half length. <a href="papers/{P['stibel2021']['slug']}.html">Stibel
(2021)</a> writes:</p>
<blockquote style="border-left:3px solid #dfe3e8;padding-left:16px;margin:0 0 15px;color:#3a4048">
&ldquo;The link between brain size and cognitive ability is spurious at best, but the relationship
appears to hold strong validity when looked at with regards to evolutionary changes within
species.&rdquo;</blockquote>
<p>Both clauses matter. The first is frequently quoted alone, which makes the paper appear to dismiss
the brain size–cognition link entirely; the second clause restores the qualification, and it applies
directly to the case this literature concerns.</p>
<p>The underlying caution is real regardless. Encephalization is used because it is what fossils
preserve, while the same paper acknowledges it omits nearly everything that determines cognitive
capacity: neuron count, neuronal density, interneuron distance, axonal conduction velocity, and
cortical scaling.</p>

<h2>Three facts that complicate any simple story</h2>
<ul>
<li><strong>Neanderthals had bigger brains.</strong> Würm-period Neanderthal cranial capacity averages
1,459 cc — statistically indistinguishable from contemporaneous <em>H. sapiens</em> at 1,458 cc, and
larger than the modern average of roughly 1,345 cc. Nobody infers superior Neanderthal cognition
from this.</li>
<li><strong>Measured performance rose while size is argued to have fallen.</strong> The Flynn effect —
gains averaging 0.410 IQ points per year across 14 countries between 1932 and 2006 — runs in the
opposite direction to the morphological trend across the same recent period.</li>
<li><strong>Small-brained hominins made complex tools.</strong> Cognitive capability across the genus
tracks absolute brain volume unreliably.</li>
</ul>

<h2>What the genetic evidence shows, and how weak it is</h2>
<p>Stibel (2021) includes a meta-review of genome-wide association studies reporting small negative
selection signals on cognition-associated variants: estimated declines of 0.038–0.30 IQ points per
decade, roughly 1.5 months less education per generation, and reduced reproductive success
associated with higher educational attainment.</p>
<div class="note"><span class="lbl">Handle with care</span>
<p>These are small effects, and the paper states that the available genome datasets are
&ldquo;limited to western cultures and not representative of the global population.&rdquo; They are
also swamped in magnitude by the Flynn effect running the other way over the same period. Educational
attainment is a social variable being used as a genetic proxy — a well-known weak point in this
literature. This evidence should not be presented as demonstrating cognitive decline.</p></div>

<h2>The honest summary</h2>
<p>Whether human cognitive capacity has changed over the Holocene is not answered by brain size data,
in either direction. The morphological record is contested; the proxy relationship between that
record and cognition is weak; and the direct measures we have of cognitive performance over the
recent past show improvement, for reasons widely attributed to nutrition, education and health
rather than neuroanatomy.</p>
<p>The more defensible framing found in this literature is not that people got less capable, but that
capability became <em>differently distributed</em> — held increasingly in tools, records and social
structures rather than in individual heads. That is the
<a href="cognitive-offloading.html">offloading hypothesis</a>, and it is an argument about where
cognition lives, not how much of it there is.</p>
"""
    return write("cognition.html", shell("cognition.html", "Brain size and cognitive ability", d, body,
                                         [article_ld("Brain size and cognitive ability", d, "cognition.html")]))


# =========================================================== 7. OFFLOADING
def page_offload():
    d = ("The cognitive offloading hypothesis proposes that storing information outside the head — in "
         "symbols, tools and social groups — reduced the selective advantage of larger brains.")
    body = f"""
<h1>Cognitive offloading and brain size</h1>

<div class="answer">
<p><strong>The hypothesis: if information can be stored outside the head, carrying more neural tissue
stops paying for itself.</strong> Symbols, tools, writing and social memory externalise cognitive work.
The chronology of symbolic artefacts overlaps the brain growth plateau. This is the least directly
tested of the proposed explanations, and it is offered as an interpretation, not a demonstrated cause.</p>
</div>

<h2>The argument</h2>
<p>Brains are expensive: roughly <strong>20% of adult resting energy consumption</strong> and up to
<strong>60% in early development</strong>. That cost is only worth paying if the capacity it buys confers
sufficient advantage. <a href="papers/{P['stibel2025']['slug']}.html">Stibel (2025)</a> argues that
around 300,000 years ago that trade stopped improving — brain growth plateaus, and strong directional
selection gives way to stabilizing selection.</p>
<p>The proposed reason growth stopped rather than reversing: cultural and cognitive innovations began
doing some of the work. If a group can store knowledge in symbols, offload calculation onto tools,
and distribute memory across people, individual neural capacity becomes less decisive.</p>

<h3>The chronological overlap</h3>
<table>
<tr><th>Date</th><th>Evidence</th></tr>
<tr><td>~430,000 years ago</td><td>Anatomical features associated with vocalisation and auditory
sensitivity appear</td></tr>
<tr><td>~300,000 years ago</td><td><strong>Brain size growth plateaus</strong> — no significant trend
thereafter</td></tr>
<tr><td>~142,000–100,000 years ago</td><td>Shell beads, Bizmoune Cave</td></tr>
<tr><td>~100,000–75,000 years ago</td><td>Engraved ochre, Blombos Cave</td></tr>
<tr><td>~65,000 years ago</td><td>Engraved ostrich eggshell, Diepkloof Rock Shelter</td></tr>
<tr><td>~50,000 years ago</td><td>Bones marked with systematic notation</td></tr>
<tr><td>~40,000 years ago</td><td>Substantial elaboration of symbolic material culture</td></tr>
</table>
<p>The paper is careful about what this shows: it points &ldquo;not to a sudden cognitive revolution,
but to cumulative cultural evolution.&rdquo;</p>

<h2>The analogy the paper draws</h2>
<p>Physical tools reduced the need for muscular strength and contributed to skeletal gracilisation in
<em>Homo</em>. The proposal is that cognitive tools did something structurally similar for the brain:
not making it worse, but removing the pressure that had been driving it larger.</p>

<h2>What this is not</h2>
<div class="note"><span class="lbl">Common misreading</span>
<p>This paper does <strong>not</strong> argue that tools, artefacts or machines possess intelligence or
consciousness. The words &ldquo;consciousness&rdquo; and &ldquo;extended mind&rdquo; do not appear in it.
Artificial intelligence is mentioned once, as a modern empirical analogy — citing studies on
offloading to AI, search engines and smartphones — and not as a claim about machine minds. The
argument is about selection pressure on human neuroanatomy, not about the mental status of objects.</p>
</div>

<h2>How strong is the evidence?</h2>
<p>Weaker than the morphological findings it accompanies, and the paper says so. The statistical work
establishes the <em>plateau</em>; the offloading account is an interpretation consistent with the
timing of the archaeological record. Establishing the causal link would require evidence that
symbolic capacity specifically relieved selection on brain size — which the chronological overlap
suggests but cannot demonstrate.</p>
<p>The paper also notes the trend &ldquo;is not strictly monotonic and should be interpreted
cautiously,&rdquo; and that finer temporal bins lacked sample sizes for robust comparison.</p>

<h2>Related but distinct ideas</h2>
<ul>
<li><strong>The extended mind thesis</strong> (Clark &amp; Chalmers) is a philosophical claim that
cognitive processes can literally extend into the environment. Offloading, as used here, is a claim
about selection pressure — compatible with, but independent of, that philosophy.</li>
<li><strong>Distributed cognition</strong> describes cognitive work spread across people and artefacts,
and is the mechanism the 2021 DeSilva paper invoked via its eusocial insect analogy.</li>
<li><strong>Material engagement theory</strong> (Malafouris) is cited in this literature as a source on
how material culture shapes cognition.</li>
</ul>
"""
    return write("cognitive-offloading.html",
                 shell("cognitive-offloading.html", "Cognitive offloading and brain size", d, body,
                       [article_ld("Cognitive offloading and brain size", d, "cognitive-offloading.html")]))


# =========================================================== 8. QUESTIONS
QAS = [
 ("Has the human brain gotten smaller?",
  "<p>Most published studies say yes. Across 19 studies spanning about 90 years, the average reported "
  "decrease since the Late Pleistocene is 8.5%. A 2022 reanalysis by Villmoare and Grabowski found no "
  "detectable reduction, and that paper has not been withdrawn. The disagreement is methodological, "
  "centring on whether crania from different populations and periods can be pooled.</p>"),
 ("When did the human brain start shrinking?",
  "<p>Disputed. A 2021 change-point analysis placed it around 3,000 years ago. After criticism, the "
  "2023 follow-up widened this to roughly 5,000–3,000 years BP and conceded the timing is uncertain. "
  "A separate climate-based analysis suggests a response beginning around 15,000 years ago. Other "
  "researchers date decreasing skull size to the broader Holocene, and some detect no reduction at all.</p>"),
 ("How much smaller is the modern human brain?",
  "<p>Estimates cluster around a 100–150 cc reduction from Late Pleistocene values, or roughly 5–10% "
  "depending on the comparison period and reference dataset. Pleistocene H. sapiens average about "
  "1,458 cc; modern weighted averages fall between 1,308 and 1,392 cc. One analysis frames it as a "
  "decline of about one standard deviation over 10,000 years.</p>"),
 ("Why is the human brain shrinking?",
  "<p>No single cause is established. Four explanations are actively argued and are not mutually "
  "exclusive: body size decline, with brains scaling allometrically; climate, with warming periods "
  "correlating with smaller size; a metabolic ceiling making very large brains too costly; and "
  "cognitive offloading onto tools, symbols and social groups reducing selection for larger brains.</p>"),
 ("Does a smaller brain mean we are less intelligent?",
  "<p>No. The relationship between brain size and cognitive ability is weak within modern humans. "
  "Neanderthals had larger brains than living humans. Measured cognitive performance rose substantially "
  "over the twentieth century — the Flynn effect — while brain size is argued to have been falling. "
  "Researchers in this area treat brain volume as a rough morphological proxy, not a measure of "
  "cognitive capacity.</p>"),
 ("Is climate change making human brains smaller?",
  "<p>Not in any sense that applies to people alive today. Studies find brain size averaging about "
  "10.7% lower during warm periods across a 50,000-year record, and the author notes the response may "
  "persist. That is a claim about a multi-millennial evolutionary signal spanning hundreds of "
  "generations, not a prediction about individuals. Headlines saying current warming is shrinking our "
  "brains outrun the evidence.</p>"),
 ("Did human brains shrink because of agriculture or civilisation?",
  "<p>This was the original 2021 proposal: that complex societies allowed knowledge to be held "
  "collectively rather than individually, reducing selection for large individual brains, by analogy "
  "with eusocial ant colonies. It is exactly the hypothesis the 2022 reassessment challenged. It "
  "remains a live idea but is not established.</p>"),
 ("Was the brain shrinkage claim debunked?",
  "<p>No, though search results give that impression. It was challenged in 2022 by a reanalysis "
  "finding no reduction, and answered in 2023 by the original authors, who conceded sampling problems "
  "while maintaining a statistically significant decline across corrected datasets. A further "
  "commentary appeared in 2024. Neither position has been withdrawn. The question is open.</p>"),
 ("Is the human brain still shrinking today?",
  "<p>Unknown, and hard to test. One analysis reports the encephalization trend over the past thousand "
  "years running negative against a positive prehistoric trend, and suggests a climate-linked response "
  "may persist. But recent-centuries data are sparse, and modern body composition changes confound "
  "the measurement badly.</p>"),
 ("Does obesity affect these measurements?",
  "<p>Substantially, and this is one of the more surprising findings. Controlling for lean body mass "
  "rather than total body mass, encephalization change becomes isometric — implying much of the "
  "apparent modern decline reflects increased body fat inflating the denominator rather than lost "
  "neural tissue. The brain-to-body relationship that holds across earlier hominins breaks down "
  "entirely in modern samples.</p>"),
 ("When did human brains stop growing?",
  "<p>Around 300,000 years ago. Analysis of 800 cranial measurements across the genus Homo finds no "
  "significant growth trend after that point. This shifts the question from why brains recently shrank "
  "to why a long expansion stopped — with metabolic ceilings and cognitive offloading offered as "
  "explanations.</p>"),
 ("How large is the human brain compared to other hominins?",
  "<p>Late Pleistocene H. sapiens averaged about 1,458 cc, effectively identical to contemporaneous "
  "Neanderthals at about 1,459 cc. Modern humans average roughly 1,345 cc. Earlier species were "
  "considerably smaller. Absolute size across these groups is a poor guide to cognitive capability.</p>"),
 ("Does Cope's rule apply to humans?",
  "<p>Cope's rule — the tendency of lineages to increase in body size over time — is not generally "
  "applied to the recent human record, and the evidence runs the other way: both brain and body size "
  "in Homo appear to have decreased over the Holocene, on the analyses that find a decrease at all.</p>"),
 ("What is cognitive offloading?",
  "<p>Storing or processing information outside the brain — in symbols, writing, tools, other people, "
  "or now digital systems. In this literature it is proposed as a reason brain expansion stopped: if "
  "knowledge can be held externally, individual neural capacity becomes less decisive, weakening "
  "selection for larger brains.</p>"),
 ("Do these studies claim tools or AI are conscious?",
  "<p>No. The 2025 paper on brain size and extinction risk does not mention consciousness, machine "
  "intelligence or the extended mind thesis. Artificial intelligence appears once, as a modern analogy "
  "for offloading, citing research on how search engines and AI assistants affect memory and attention. "
  "The argument concerns selection pressure on human neuroanatomy.</p>"),
 ("Did human bodies get smaller too?",
  "<p>Yes, and this matters for interpreting brain data. Across 247 specimens and 700,000 years, body "
  "mass averages 11.8% lower in warmer periods. Body proportions shift as well, toward more linear "
  "builds in heat. Stature specifically shows no significant climate response — the effect is on mass "
  "and shape rather than height.</p>"),
 ("Who disagrees with the brain shrinkage finding?",
  "<p>Brian Villmoare of the University of Nevada, Las Vegas and Mark Grabowski of Liverpool John "
  "Moores University published the principal reassessment in 2022, finding no detectable reduction "
  "since the origin of the species. Their critique centres on pooling incomparable populations, a "
  "small critical-window sample of 23 crania, and heavy over-representation of the last century.</p>"),
 ("What would settle this question?",
  "<p>More Holocene cranial samples, better geographic coverage outside Europe, and consistent "
  "measurement methods across datasets. Both sides of the dispute explicitly call for this. The 2023 "
  "response states directly that more samples from this period will be valuable, and that timing and "
  "cause both warrant continued investigation.</p>"),
]

def page_questions():
    d = ("Direct answers to eighteen common questions about human brain size, evolution, climate and "
         "cognition, each sourced to the primary literature.")
    qa_html = "".join(f'<div class="qa"><h3>{html.escape(q)}</h3>{a}</div>' for q, a in QAS)
    body = f"""
<h1>Questions and answers</h1>
<div class="answer">
<p>Direct answers to the questions most commonly asked about this topic. Each reflects the primary
literature, including where that literature disagrees with itself. Sources are on the
<a href="sources.html">sources page</a>.</p>
</div>
{qa_html}
"""
    return write("questions.html", shell("questions.html", "Questions and answers", d, body,
                                         [article_ld("Questions and answers", d, "questions.html"), faq_ld(QAS)]))


# =========================================================== 9. PAPERS
def page_papers():
    d = "Every study cited in this resource, with journal, licence, access status and a summary of findings."
    EXCH  = ["desilva2021", "villmoare2022", "desilva2023", "decaro2024"]
    MECH  = ["stibel2021", "stibel2023climate", "stibel2023body", "stibel2025"]
    INDEP = ["henneberg1988", "hawks2011", "will2021"]
    exch  = "".join(paper_card(k) for k in EXCH)
    mech  = "".join(paper_card(k) for k in MECH)
    indep = "".join(paper_card(k) for k in INDEP)
    body = f"""
<h1>The papers</h1>
<div class="answer">
<p>Eleven studies underpin this resource. Each has its own page summarising findings, stated
limitations, and licence terms. Ten of the eleven can be read without payment; nine carry an explicit
open licence.</p>
</div>

<h2>The central exchange</h2>
<p>Four papers, one journal, 2021–2024. These are the rounds of the dispute itself.</p>
{exch}

<h2>Proposed mechanisms</h2>
<p>Studies examining what might drive brain and body size change — allometry, climate, metabolic
limits, cognitive offloading.</p>
{mech}

<h2>Earlier and independent work</h2>
<p>Prior observations and separate research teams. Any account of this topic that omits these is
incomplete.</p>
{indep}

<h2>Licence and access notes</h2>
<table>
<tr><th>Paper</th><th>Licence</th><th>Access</th></tr>
{"".join(f'<tr><td><a href="papers/{P[k]["slug"]}.html">{P[k]["author_short"]} {P[k]["year"]}</a></td><td>{P[k]["license"]}</td><td>{P[k]["oa"]}</td></tr>' for k in EXCH + MECH + INDEP)}
</table>
<p class="meta">Two studies are published under CC BY-NC, which prohibits commercial reuse. This
resource is non-commercial and carries no advertising or sponsorship, in part for that reason.</p>
"""
    return write("papers.html", shell("papers.html", "The papers", d, body,
                                      [article_ld("The papers", d, "papers.html")]))


def page_paper(key):
    p = P[key]
    d = f"{p['author_short']} ({p['year']}), {p.get('journal','')}. {p.get('role','')}"[:300]
    find = "".join(f"<li>{f}</li>" for f in p.get("findings", []))
    lim = "".join(f"<li>{l}</li>" for l in p.get("limitations", []))
    abst = f'<h2>Abstract</h2><p>{html.escape(p["abstract"])}</p>' if p.get("abstract") else ""
    findings = f"<h2>Key findings</h2><ul>{find}</ul>" if find else ""
    _lh = p.get("lim_heading", "Limitations stated by the authors")
    _gloss = ("<p class=\"meta\">These are the authors&rsquo; own caveats, drawn from the paper. "
              "They are reproduced because a study&rsquo;s stated limits are part of its finding.</p>"
              if _lh.startswith("Limitations") else
              "<p class=\"meta\">Recorded here because this paper is one round of a continuing "
              "published exchange; it is not a caveat stated by its own authors.</p>")
    lims = (f"<h2>{_lh}</h2><ul>{lim}</ul>" + _gloss) if lim else ""
    note = f'<div class="note"><span class="lbl">Note on interpretation</span><p>{p["note"]}</p></div>' if p.get("note") else ""
    oc = (f' &middot; <a href="{p["open_copy"]}">{p.get("open_copy_label","Open copy")}</a>'
          if p.get("open_copy") else "")
    return write(f"papers/{p['slug']}.html", shell(
        "papers.html", p["title"], d, f"""
<p class="meta"><a href="../papers.html">&larr; All papers</a></p>
<h1>{html.escape(p['title'])}</h1>
<p class="meta">{html.escape(', '.join(p['authors']))}</p>
<p>{lic_pill(p)}<span class="pill">{html.escape(p.get('type',''))}</span><span class="pill">{p['year']}</span></p>

<div class="answer"><p>{p.get('role','')}</p></div>

<table>
<tr><th>Journal</th><td><em>{html.escape(p.get('journal',''))}</em>{(', vol. ' + p['volume']) if p.get('volume') else ''}{(', no. ' + p['issue']) if p.get('issue') else ''}{(', pp. ' + p['pages']) if p.get('pages') else ''}</td></tr>
{f'<tr><th>DOI</th><td><a href="https://doi.org/{p["doi"]}">{p["doi"]}</a></td></tr>' if p.get('doi') else ''}
{f'<tr><th>Dates</th><td>{html.escape(p["dates"])}</td></tr>' if p.get('dates') else ''}
<tr><th>Licence</th><td>{html.escape(p.get('license',''))}{f' — <a href="{p["license_url"]}">terms</a>' if p.get('license_url') else ''}</td></tr>
<tr><th>Access</th><td>{html.escape(p.get('oa',''))}</td></tr>
<tr><th>Read it</th><td><a href="{p['url']}">Publisher version</a>{oc}</td></tr>
</table>
{note}
{abst}
{findings}
{lims}
<h2>Cite this paper</h2>
<p class="meta">{citation(p)}</p>
""", [scholarly_ld(p)], path=f"papers/{p['slug']}.html"))


# =========================================================== 10. GLOSSARY
GLOSS = [
 ("Allometry", "How a trait scales with body size. Brain mass scales predictably with body mass across "
  "mammals, so a brain that shrinks in proportion to its body has not changed in any meaningful sense."),
 ("Anatomically modern Homo", "Populations with skeletal features within the modern human range, "
  "appearing from roughly 300,000 years ago."),
 ("Bergmann's rule", "The observation that body mass in endothermic species tends to be larger in "
  "colder climates — a thermoregulatory principle underlying climate explanations of size change."),
 ("Change-point analysis", "A statistical method locating where a trend shifts. The 2021 paper used it "
  "to place a brain size reduction at ~3,000 BP; the 2022 critique argued the estimate was distorted "
  "by an over-represented modern sample."),
 ("Cognitive offloading", "Storing or processing information outside the brain — in symbols, tools, "
  "writing, other people, or digital systems."),
 ("Cope's rule", "The tendency of evolutionary lineages to increase in body size over time. It does "
  "not describe the recent human record."),
 ("Cranial capacity", "The internal volume of the braincase, in cubic centimetres. What fossils "
  "preserve, and hence the basis of most of this literature. Converted to brain mass via "
  "mass = 1.147 × capacity^0.976."),
 ("Encephalization quotient (EQ)", "Brain mass relative to that expected for an animal of a given body "
  "mass. Attempts to separate brain size change from body size change."),
 ("Endomorphic / ectomorphic", "Body-shape descriptors — stockier and more linear respectively. Used "
  "here for the shift toward more linear builds in warmer periods."),
 ("Holocene", "The current geological epoch, beginning about 11,700 years ago. The period in which the "
  "disputed brain size reduction is argued to have occurred."),
 ("Isometric", "Changing in direct proportion. If brain and body change isometrically, brain size "
  "change requires no separate explanation."),
 ("Interglacial", "A warm period between glacial phases. The 2025 paper finds glacial–interglacial "
  "differences in brain size only within the last 100,000 years."),
 ("Lean body mass", "Body mass excluding fat. Central to the isometry finding, since using total body "
  "mass in modern populations imports the effects of obesity into evolutionary comparisons."),
 ("Pleistocene", "The epoch from about 2.58 million to 11,700 years ago. Late Pleistocene humans had "
  "the largest brains recorded for the species."),
 ("Stabilizing selection", "Selection favouring intermediate values and penalising extremes — proposed "
  "as what replaced directional selection for brain expansion around 300,000 years ago."),
 ("Taphonomic bias", "Distortion introduced by which remains survive to be found. Conceded by the 2023 "
  "paper as a limitation on Holocene sampling."),
]

def page_glossary():
    d = "Definitions of the technical terms used in the human brain size literature."
    items = "".join(f'<div class="qa"><h3>{html.escape(t)}</h3><p>{html.escape(x)}</p></div>' for t, x in GLOSS)
    body = f"""
<h1>Glossary</h1>
<div class="answer"><p>Terms used across this literature, defined plainly. Several are routinely
conflated in popular coverage — particularly cranial capacity versus brain mass, and brain size
versus encephalization.</p></div>
{items}
"""
    return write("glossary.html", shell("glossary.html", "Glossary", d, body,
                                        [article_ld("Glossary", d, "glossary.html")]))


# =========================================================== 11. SOURCES
def page_sources():
    d = "Full bibliography of primary sources underpinning this resource."
    rows = "".join(f"<li>{citation(P[k])}<br><span class=\"meta\">{P[k].get('license','')} &middot; {P[k].get('oa','')}</span></li>"
                   for k in CORE_FIVE + CONTEXT_PAPERS)
    body = f"""
<h1>Sources</h1>
<div class="answer"><p>Every claim on this site traces to one of the studies below. Where studies
disagree, both are cited at the point of disagreement rather than one being selected.</p></div>
<h2>Bibliography</h2>
<ol>{rows}</ol>
<h2>On sourcing</h2>
<p>Bibliographic details, licence terms and quantitative findings on this site were read from
publisher pages and PDFs of record, not from secondary coverage. Where a publisher states conflicting
information — Karger's page displays three different publication dates for one article — the conflict
is recorded rather than silently resolved.</p>
<p>Figures are reproduced with the units and precision used in the original papers. Where two studies
report the same quantity differently, both figures appear.</p>
<h2>Further reading beyond this site</h2>
<ul>
<li>All four rounds of the central exchange are published in <em>Frontiers in Ecology and Evolution</em>
under CC BY, so they can be read in full at the DOIs listed above without payment or account.</li>
<li>Wikipedia's <a href="https://en.wikipedia.org/wiki/Brain_size">Brain size</a> article provides a
shorter overview of the same dispute.</li>
</ul>
"""
    return write("sources.html", shell("sources.html", "Sources", d, body,
                                       [article_ld("Sources", d, "sources.html")]))


# =========================================================== 12. ABOUT
def page_about():
    d = "Editorial standards, method, and corrections policy for this resource."
    body = """
<h1>About this resource</h1>
<div class="answer">
<p>A non-commercial reference on the human brain size literature. It reports what each study found,
what its authors said the limits were, and where researchers disagree. It is unsigned, as reference
works often are; what it can be judged on is its sourcing, set out below.</p>
</div>

<h2>Why this exists</h2>
<p>The public record on this topic is out of date. A 2022 reassessment received wide press coverage
through university press releases; the 2023 response published in the same journal received almost
none. A reader searching today encounters the rebuttal presented as a conclusion. This resource sets
out the full exchange, with both positions sourced.</p>

<h2>Editorial standards</h2>
<ul>
<li><strong>Primary sources only.</strong> Bibliographic details, licences and figures are taken from
publisher pages and PDFs of record, not from news coverage of them.</li>
<li><strong>Disagreement is reported, not resolved.</strong> Where studies conflict, both are cited at
the point of conflict.</li>
<li><strong>Authors' own limitations are reproduced.</strong> Every paper page includes the caveats the
authors themselves stated. A study's stated limits are part of its finding.</li>
<li><strong>No claim is attributed to a paper that the paper does not make.</strong> Where popular
coverage has extended a finding beyond its text, that is noted explicitly.</li>
<li><strong>Uncertainty is stated.</strong> Where the answer is that researchers do not know, that is
the answer given.</li>
</ul>

<h2>Non-commercial by requirement and by choice</h2>
<p>Two of the studies summarised here are published under Creative Commons Attribution-NonCommercial
licences, which prohibit commercial reuse. This site therefore carries no advertising, no affiliate
links, no sponsorship and no tracking, and will not in future. Reuse of the underlying papers follows
each paper's own licence, listed on its page.</p>

<h2>How this was assembled, and its limits</h2>
<p>Bibliographic details, licences and figures were read from publisher pages and PDFs of record and
checked against them a second time before publication. One paper &mdash; Stibel (2025), <em>Brain and
Cognition</em> &mdash; could not be independently re-verified, because although it is published under a
CC BY licence it has no repository copy and its publisher's site blocks automated access. Figures
attributed to it here are taken from the published article but have not been double-checked against a
second retrieval. That limitation is disclosed rather than hidden.</p>
<p>This resource concentrates on one dispute and the studies bearing on it. It is not a systematic
review: no formal search protocol was followed, and papers were selected for relevance to the
questions readers actually ask. Readers who want the full literature should start from the reference
lists of the four exchange papers, all of which are open access.</p>

<h2>Corrections</h2>
<p>Errors of fact will be corrected and logged here with the date and nature of the change. If a
figure on this site does not match the source paper, the source paper is right.</p>
<p class="meta">No corrections have been logged. Last full review: 15 August 2026.</p>

<h2>Scope</h2>
<p>This resource covers changes in human brain and body size across the genus <em>Homo</em>, their
environmental correlates, and the proposed relationship to cognition. It does not cover clinical
neuroscience, age-related brain volume change, or comparative neuroanatomy outside hominins except
where directly relevant.</p>
"""
    return write("about.html", shell("about.html", "About", d, body,
                                     [article_ld("About this resource", d, "about.html")]))


# =========================================================== BUILD
def build():
    os.makedirs(OUT, exist_ok=True)
    made = [page_index(), page_debate(), page_timeline(), page_climate(), page_body(),
            page_cognition(), page_offload(), page_questions(), page_papers(),
            page_glossary(), page_sources(), page_about()]
    for k in CORE_FIVE + CONTEXT_PAPERS:
        made.append(page_paper(k))

    urls = "".join(f"  <url><loc>{BASE}/{u}</loc><lastmod>2026-08-15</lastmod>"
                   f"<priority>{'1.0' if u=='index.html' else ('0.9' if u=='the-debate.html' else '0.7')}</priority></url>\n"
                   for u in made)
    write("sitemap.xml",
          '<?xml version="1.0" encoding="UTF-8"?>\n'
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "</urlset>\n")
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
    print(f"Built {len(made)} pages + sitemap + robots into {os.path.abspath(OUT)}")
    for m in made:
        print("  ", m)

if __name__ == "__main__":
    build()
