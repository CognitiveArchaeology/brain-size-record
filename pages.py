# -*- coding: utf-8 -*-
"""Page content for the reference hub. Run this file to build the site."""
import os, re, json, html
from papers import PAPERS, CORE_FIVE, CONTEXT_PAPERS, citation, LIT, lit, src, sources, yr
from build import (shell, write, paper_card, lic_pill, scholarly_ld,
                   article_ld, faq_ld, OUT, NAV, BASE, SITE_NAME, TAGLINE)

P = PAPERS

# =========================================================== 1. OVERVIEW
def page_index():
    d = ("Human cranial capacity expanded through the Pleistocene, plateaued around 300,000 years "
         "ago, and appears to have declined during the Holocene. The timing, the cause, and in one "
         "reanalysis the finding itself remain contested. A sourced account of the evidence.")
    body = f"""
<h1>Has the human brain gotten smaller?</h1>

<div class="answer">
<p><strong>Over evolutionary time, most of the evidence says the human brain has recently shrunk by
a surprising amount.</strong> Endocranial volume roughly tripled across the hominin lineage and
roughly doubled within <em>Homo</em>, stopped growing around 300,000 years ago, and declined during
the Holocene by something on the order of 5 to 10 percent. The size of that decline, its timing and
its cause are all argued over, and a 2022 reanalysis found no statistically supported reduction at
all.</p>
</div>

<p class="upd">Reviewed 15 August 2026</p>

<h2>The long record</h2>

<p>The expansion is not in dispute. Endocranial volume across the genus grows through the Early and
Middle Pleistocene, with <a href="papers/{P['desilva2023']['slug']}.html">statistically significant
shifts in the rate of change</a> around 2.0 and 1.5 million years ago. Stibel (2025), analysing
<a href="papers/{P['stibel2025']['slug']}.html">800 cranial measurements</a>, finds the growth trend
disappearing about 300,000 years ago, after which the record is flat. Neubauer, Hublin and Gunz
(2018) reach a compatible conclusion from a different direction: volume was already within the
modern range in the earliest <em>H. sapiens</em>, and what changed afterwards was endocranial shape.</p>

<p>The decline comes later and is still contested but largely confirmed. Henneberg (1988) documented
decreasing skull size across Holocene European series, and Henneberg and Steyn (1993) found the same
pattern in a sub-Saharan African sample.
<a href="papers/{P['desilva2023']['slug']}.html">DeSilva et al. (2023)</a> put the average reported
decrease across 19 studies at 8.5 percent, with Pleistocene <em>H. sapiens</em> averaging 1,458 cc
against a modern figure near 1,345 cc.
<a href="papers/{P['stibel2021']['slug']}.html">Stibel (2021)</a> puts it at 5.4 percent relative to
the Upper Palaeolithic, using matched cranial and postcranial remains so that body size is
controlled. <a href="timeline.html">The full chronology</a> sets these against each other.</p>

<h2>Where researchers disagree</h2>

<table>
<tr><th>Question</th><th>Positions taken</th></tr>
<tr><td>Is a Holocene reduction statistically supported?</td>
<td>Yes, on most published datasets.
<a href="papers/{P['villmoare2022']['slug']}.html">Villmoare and Grabowski's (2022)</a> analysis is
the only published analysis to find no significant change point, arguing the effect comes from
uneven sampling. That was contested by
<a href="papers/{P['desilva2023']['slug']}.html">DeSilva et al. (2023)</a>, who corrected their
dataset and reaffirmed the decline.</td></tr>
<tr><td>What is the modern human average?</td>
<td>Estimates run from about 1,297 cc to 1,460 cc, depending on which population was measured and
by whom.</td></tr>
<tr><td>Does brain size track body size?</td>
<td>Ruff, Trinkaus and Holliday (1997) showed endocranial trends cannot be interpreted without a
matched body mass series. <a href="papers/{P['stibel2021']['slug']}.html">Stibel (2021)</a> finds the
change isometric once lean body mass is controlled.</td></tr>
<tr><td>Is climate the driver?</td>
<td><a href="papers/{P['stibel2023climate']['slug']}.html">Stibel (2023a)</a> finds temperature
predicts both brain and body size. Will et al. (2021) find temperature predicts body size well and
brain size only weakly and indirectly.</td></tr>
<tr><td>Is volume the right variable?</td>
<td>Neubauer et al. (2018) argue the informative change after 300,000 years ago was in shape, not
size. Logan et al. (2018) make the broader case that gross volume conflates independently evolving
components.</td></tr>
</table>

<h2>Proposed explanations</h2>

<p>If a reduction occurred, several mechanisms have been offered. They are not exclusive, and none is
established.</p>

<div class="card"><h3>Body size</h3>
<p>Brains scale with bodies. Controlled for lean body mass the change looks isometric, which would
make much of the measured decline in encephalization an artefact of rising modern body fat rather
than lost neural tissue. Ruff, Trinkaus and Holliday (1997) made the general form of this argument.
<a href="body-size.html">More</a></p></div>

<div class="card"><h3>Climate</h3>
<p>Body mass in warmer periods runs roughly 12% lower across 700,000 years, consistent with a long
literature on thermoregulation and body form running back to Roberts in 1953. Whether brain size
follows the same signal is disputed. <a href="climate.html">More</a></p></div>

<div class="card"><h3>Metabolic cost</h3>
<p>Brain tissue is expensive. Kuzawa et al. (2014) measured childhood brain glucose use at roughly
two thirds of resting metabolic rate. Fonseca-Azevedo and Herculano-Houzel (2012) identified a feeding-time
ceiling on how many neurons a primate can support. Beyond some point the tissue may stop paying for
itself. <a href="papers/{P['stibel2025']['slug']}.html">More</a></p></div>

<div class="card"><h3>Information held outside the head</h3>
<p>Writing, tools, records and other people all store what a brain would otherwise carry. If capacity
can sit outside the skull, selection for carrying more of it weakens.
<a href="cognitive-offloading.html">More</a></p></div>

<div class="card"><h3>Self-domestication</h3>
<p>Domesticated mammals show brain reductions of 8 to 30 percent. Selection for social tolerance in
humans has been argued to produce the same developmental signature, with Cieri et al. (2014)
documenting facial and brow reduction over the same period. The parallel is contested.
<a href="self-domestication.html">More</a></p></div>

<h2>The last century is a separate question</h2>

<p>Measurements of living and recently deceased people run the other way. Miller and Corsellis (1977) found brain weight rising across the twentieth century in a large autopsy series. Jantz and Jantz (2016) document substantial change in Euro-American cranial size and shape across roughly 150 years. DeCarli et al. (2024), using MRI in Framingham Heart Study participants born between 1930 and 1970, found
intracranial and cerebral volumes increasing across birth decades.</p>

<p>None of this bears on the evolutionary trend, and it is a mistake to set the two against each
other. Forty birth years is about a generation and a half. Selection does not operate on that scale;
growth does. Nutrition, childhood disease burden, birth weight, maternal health and stature all
improved sharply over the same period, and skeletal dimensions track them, which is why stature rose
in the same populations at the same time. What the modern series measures is developmental
plasticity within a fixed genetic range, not a change in that range.</p>

<p>The practical consequence is a limit on what any recent sample can tell you. Modern reference
values are used as the endpoint in every fossil comparison, so a secular trend in those values feeds
directly into estimates of how much the brain has declined. It is a reason to treat the modern
number carefully.</p>

<h2>What this does not show</h2>

<div class="note"><span class="lbl">Frequently misstated</span>
<p>Smaller does not mean less capable. Within living humans, brain volume and measured intelligence
correlate somewhere between r = .19 and r = .40 depending on sample and measurement quality, which
leaves most variance unexplained either way. Neanderthals had larger brains than living humans.
Measured cognitive performance rose by roughly three IQ points per decade through the twentieth
century, and Norwegian conscript data (Bratsberg and Rogeberg 2018) show that rise and its later reversal are both environmental.
<a href="cognition.html">More on brain size and cognition</a></p></div>

<h3>Sources on this page</h3>
{sources(['desilva2023', 'stibel2021', 'stibel2023climate', 'stibel2023body', 'stibel2025', 'villmoare2022', 'henneberg1988', 'hennebergsteyn1993', 'ruff1997', 'roberts1953', 'neubauer2018', 'logan2018', 'kuzawa2014', 'fonseca2012', 'cieri2014', 'kruska2005', 'miller1977', 'jantz2016', 'decarli2024'])}
"""
    return write("index.html", shell("index.html", SITE_NAME, d, body,
                                     [article_ld("Has the human brain gotten smaller?", d, "index.html")]))


# =========================================================== 2. THE DEBATE
def page_debate():
    d = ("Whether human cranial capacity declined during the Holocene has been argued in print since "
         "1988 and remains unsettled. The evidence on each side, including the reanalyses.")
    body = f"""
<h1>Did human brains shrink in the Holocene?</h1>

<div class="answer">
<p><strong>The data supports a decrease in brain size somewhere within the last 100,000 years.</strong>
The observation is not new; the interpretation now has more evidence and support. An early study
reported decreasing Holocene skull size as early as 1988. Multiple recent studies have pointed
specifically to a number of causes, alongside greater evidence. One study pointed to methodological
issues that make determining the exact trend difficult without additional data.</p>
</div>

<h2>Where the observation came from</h2>

<p>Henneberg (1988) reported a decreasing trend in cranial size across Holocene European series in
the journal <em>Human Biology</em>. Henneberg and Steyn (1993) extended the finding to a sub-Saharan
African sample, which mattered because it tested whether the pattern was regional or general. Beals,
Smith and Dodd (1984) had already assembled the large comparative dataset relating cranial capacity
to climate, published with commentary from Henneberg, Trinkaus and others, so the disagreements
about interpretation are as old as the data.</p>

<p>None of this was controversial in the way the recent exchange has been. The dispute is not about
whether the measurements exist. It is about what they support.</p>

<h2>The recent exchange</h2>

<div class="round r1">
<span class="yr">2021</span>
<h3><a href="papers/{P['desilva2021']['slug']}.html">DeSilva, Traniello, Claxton and Fannin</a></h3>
<p>Change-point analysis on a large compilation of fossil and recent crania placed a reduction at
roughly 3,000 years BP. The proposed mechanism was externalisation of information into social groups,
drawn by analogy to reduced brain size in eusocial ant colonies. The ant comparison made the paper
unusually quotable and it was covered widely.</p>
</div>

<div class="round r2">
<span class="yr">2022</span>
<h3><a href="papers/{P['villmoare2022']['slug']}.html">Villmoare and Grabowski</a></h3>
<p>Reanalysing portions of the same dataset, they found no reduction detectable since the origin of
the species, and concluded human brain size has been "remarkably stable over the last 300 ka."</p>
<p>Their objections were both about sampling and about statistics. On sampling: the dataset pools
specimens from England, China, Mali and Algeria as though comparable; only 23 crania fall inside the
critical window; and 578 of roughly 987 specimens come from the final century of a span covering
some 9.8 million years. On statistics: the original change point was never tested for significance,
and applying a Davies test returns p = 0.621 on the full data. They also argued the modern reference
value of about 1,297 cc sits well below other published estimates ranging up to 1,460 cc, which
would produce an apparent decline arithmetically.</p>
</div>

<div class="round r3">
<span class="yr">2023</span>
<h3><a href="papers/{P['desilva2023']['slug']}.html">DeSilva, Fannin, Cheney, Claxton, Ilie&#537;, Kittelberger, Stibel and Traniello</a></h3>
<p>The reply conceded ground and held the central claim. Conceded: the Holocene portion of the
dataset is skewed toward modern specimens, which may pull the change point too recent and could
obscure earlier ones. Four juvenile Neanderthal specimens and a duplicate entry were removed, as was
the Morton Collection. Removing it did not appreciably change the modern estimate.</p>
<p>Maintained: across 19 published studies spanning about 90 years the average reported decrease is
8.5%, and the Pleistocene-Holocene difference remains significant when tested against two independent
modern reference datasets (Dekaban and Sadowsky 1978, n = 3,399; Beals et al. 1984, n = 5,288) as well as their
own sample. The title concedes the timing question. The
authors' position becomes that a reduction occurred, that its date is uncertain across roughly
5,000 to 3,000 BP, and that the question warrants more work.</p>
</div>

<div class="round r4">
<span class="yr">2024</span>
<h3><a href="papers/{P['decaro2024']['slug']}.html">De Caro</a></h3>
<p>A short commentary working entirely from the DeSilva dataset, with no new specimens. It recomputes
a modern reference value of 1,341 &plusmn; 130 cc from four sex-balanced samples (Dekaban and Sadowsky 1978; Ho et al. 1980; Beals et al. 1984), argues that a
25-cranium subset from Afalou, Algeria is male-biased and should be excluded, and reports that the
reduction holds without it. It also argues the decline runs continuously from the Late Pleistocene
rather than beginning at 3&ndash;5 ka. The sex-balance inference is drawn from histogram shape rather
than osteological sexing.</p>
</div>

<h2>What the wider literature adds</h2>

<p>Three findings from outside this exchange bear directly on it.</p>

<p>Ruff, Trinkaus and Holliday established in <em>Nature</em> in 1997 that endocranial volume trends
cannot be interpreted without a matched body mass series, because body size changed over the same
period. Any claim about brain size that does not control for body size is incomplete on its face.
<a href="papers/{P['stibel2021']['slug']}.html">Stibel's 2021 analysis</a> was built to address
exactly this, and found the change isometric once lean body mass is controlled.</p>

<p>Neubauer, Hublin and Gunz showed in 2018 that endocranial volume was already within the modern
range in the earliest <em>H. sapiens</em> around 300,000 years ago. What changed subsequently was
endocranial <em>shape</em>, which became globular gradually between roughly 100,000 and 35,000 years
ago. On this reading the interesting variable was never volume.</p>

<p>Du et al. (2018) demonstrated that conclusions about the pattern and pace of hominin
brain size change are scale-dependent: how the data are binned substantially affects what trend
appears. That cuts against both sides of the Holocene dispute.</p>

<h2>Why the modern endpoint is the weak link</h2>

<p>Every estimate of how much the brain has declined is a subtraction, and the number being
subtracted comes from living or recently deceased people. That endpoint is not stable.</p>

<p>Miller and Corsellis (1977) reported that brain weight had been rising across the twentieth
century in a large autopsy series. Jantz and Jantz (2016) have documented substantial change in Euro-American cranial size and shape across roughly 150 years. DeCarli et al. (2024), using MRI in
the Framingham cohort, found intracranial and cerebral volumes increasing across birth decades from
1930 to 1970.</p>

<p>These are secular trends, not evolutionary ones. A century and a half is four or five generations
and forty birth years is barely more than one, which is far too short for selection to move a
polygenic trait. What moves on that scale is growth: nutrition, infection load, birth weight and
maternal health all improved over the same period, and stature rose alongside cranial dimensions in
the same populations.</p>

<p>So this does not rebut a Holocene decline; it measures something else. What it does establish is
that the modern reference value depends on which population was measured and when, which is exactly
the point Villmoare and Grabowski press when they note published modern means ranging from about
1,297 to 1,460 cc. A 150 cc spread in the endpoint is roughly the size of the entire effect under
dispute.</p>

<h2>Where that leaves it</h2>

<ul>
<li>Neither the 2022 reanalysis nor the 2023 reply has been withdrawn or superseded.</li>
<li>The disagreement is methodological: whether crania from different populations and periods can be
pooled, what the modern reference value should be, and whether the change point survives significance
testing.</li>
<li>The observation predates the dispute by more than three decades and rests on multiple
independent datasets.</li>
<li>Independent evidence has since been added on the climate side.
<a href="papers/{P['stibel2023climate']['slug']}.html">Stibel (2023a)</a> tested temperature,
humidity and precipitation against cranial capacity in 298 <em>Homo</em> specimens across 50,000
years and found brain size averaging about 10.7 percent lower in warm periods than cool ones, with
the response beginning around 15,000 years ago. That is a decline located by a different dataset,
a different method and a different proposed mechanism from the change-point analysis under
dispute. <a href="climate.html">More on climate</a></li>
<li>The same holds on the technology side.
<a href="papers/{P['stibel2025']['slug']}.html">Stibel (2025)</a> analysed 800 cranial measurements
across the genus and found brain size growth ending around 300,000 years ago, with the subsequent
record tracking the appearance of symbolic artefacts, notation and increasingly sophisticated
material culture. On that reading the decline follows a shift in where information is held rather
than a change in what brains could do. <a href="cognitive-offloading.html">More on offloading</a></li>
<li>Recent secular change in cranial dimensions is well documented, runs upward, and reflects growth
conditions rather than selection. It bears on the accuracy of the modern endpoint, not on whether
the prehistoric trend occurred.</li>
</ul>

<h3>Sources on this page</h3>
{sources(['desilva2021', 'villmoare2022', 'desilva2023', 'decaro2024', 'stibel2021', 'stibel2023climate', 'stibel2025', 'henneberg1988', 'hennebergsteyn1993', 'beals1984', 'ruff1997', 'roberts1953', 'neubauer2018', 'du2018', 'miller1977', 'jantz2016', 'decarli2024'])}
"""
    return write("the-debate.html",
                 shell("the-debate.html", "Did human brains shrink in the Holocene?", d, body,
                       [article_ld("Did human brains shrink in the Holocene?", d, "the-debate.html")]))


# =========================================================== 3. TIMELINE
def page_timeline():
    d = ("A chronology of brain size across the genus Homo, from early expansion through the "
         "plateau around 300,000 years ago to the disputed Holocene decline.")
    body = f"""
<h1>Timeline of brain size in <em>Homo</em></h1>

<div class="answer">
<p><strong>Brain size expanded, then stopped.</strong> Endocranial volume roughly tripled across the
hominin lineage from australopith values near 445 cc, and roughly doubled within <em>Homo</em> from
early values near 683 cc. Expansion dominates the Early and Middle Pleistocene. Growth flattens around 300,000 years ago. Late Pleistocene humans and
Neanderthals converge near 1,460 cc. Modern averages sit near 1,300–1,350 cc, a gap whose
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
<td><strong>Disputed.</strong> The window in which a reduction is argued to have occurred, and in which a
reanalysis finds none</td>
<td>DeSilva 2021/2023; Villmoare &amp; Grabowski 2022</td></tr>
<tr><td>Last 1,000 years</td>
<td>Encephalization trend reverses sign (<em>r</em> = −0.483) against a positive prehistoric trend
(<em>r</em> = 0.777)</td>
<td>Stibel 2021</td></tr>
<tr><td>Present</td>
<td>Modern estimates range 1,308–1,392 cc, weighted average <strong>1,345 cc</strong> (n = 8,961).
Other published modern means run from about 1,297 to 1,460 cc</td>
<td>DeSilva et al. 2023; Villmoare &amp; Grabowski 2022</td></tr>
<tr><td><em>Last ~150 years<br>(not part of the above)</em></td>
<td><em>Directly measured brain weight and intracranial volume increase. Too few generations for
selection; attributed to nutrition, disease burden and growth conditions</em></td>
<td><em>Miller &amp; Corsellis 1977; Jantz &amp; Jantz 2016; DeCarli et al. 2024</em></td></tr>
</table>

<div class="note"><span class="lbl">Most recent sample of modern humans</span>
<p>All but the last row demonstrate evolutionary changes in brain size, describing change in what
populations inherit. The final row spans a few generations and describes how well individuals grew.
Both are valid and both are measured carefully, but only one of them is evolution. They are placed
together here because they are routinely conflated, and because the modern figures are the endpoint
every prehistoric comparison subtracts from.</p></div>

<div class="note"><span class="lbl">Units differ between rows</span>
<p>Different rows use different units. Cranial capacity in cubic centimetres and brain mass in grams
are related but not interchangeable. Stibel (2021, 2023a, 2025) converts using Ruff et al.'s (1997) equation,
brain mass = 1.147 &times; (cranial capacity)<sup>0.976</sup>; DeSilva et al. (2023) average two published
equations instead. Comparisons across rows drawn from different studies are indicative, not precise.</p></div>

<h2>The shape of the curve matters more than any single number</h2>
<p>Expansion through the Pleistocene is well established and largely uncontroversial. The plateau at
~300,000 BP is a recent finding from a large single-analysis dataset,
<a href="papers/{P['stibel2025']['slug']}.html">Stibel (2025)</a>, drawn from 800 cranial capacity
measurements across the genus, and Neubauer et al. (2018) reach a compatible result by a different
route. The Holocene decline is still under active investigation and not confirmed in terms of
magnitude, direction or timing. More data is ultimately going to be necessary.</p>

<h3>Sources on this page</h3>
{sources(['desilva2023', 'desilva2021', 'villmoare2022', 'stibel2021', 'stibel2023climate', 'stibel2025', 'neubauer2018', 'du2018', 'ruff1997', 'miller1977', 'jantz2016', 'decarli2024'])}
"""
    return write("timeline.html", shell("timeline.html", "Timeline of brain size in Homo", d, body,
                                        [article_ld("Timeline of brain size in Homo", d, "timeline.html")]))


# =========================================================== 4. CLIMATE
def page_climate():
    d = ("Temperature predicts human body size across a long literature. Whether it also predicts "
         "brain size is disputed, with two recent analyses reaching different answers.")
    body = f"""
<h1>Climate, body size and brain size</h1>

<div class="answer">
<p><strong>The body size relationship is well established. The brain size relationship is less
settled.</strong> Human body mass tracks temperature across populations and across the fossil
record. One recent analysis of brain size and climate finds temperature a substantial predictor and
another finds a weak and possibly indirect correlation.</p>
</div>

<h2>Body form and temperature</h2>

<p>Roberts (1953) established the basic relationship. Ruff's cylindrical body model, developed
through the early 1990s, identified body <em>breadth</em> rather than stature as the climatically
constrained dimension, and Ruff (1994) remains the standard treatment. Katzmarzyk and Leonard (1998)
restudied the question across 418 samples, confirming the association while noting the slopes had
grown shallower since Roberts, which they attributed to twentieth-century nutritional change.</p>

<p>Nearly all of that work is drawn from living populations.
<a href="papers/{P['stibel2023body']['slug']}.html">Stibel (2023b)</a> extends it into deep time
against the paleoclimate record, and finds the same direction of effect at the same rough magnitude,
including the specific prediction that climate should act on mass and breadth rather than height.
The figures are below.</p>

<h3>How firm is the rule</h3>

<p>Less firm than its popularity suggests. Foster and Collard (2013) found that Bergmann's rule holds
in humans only across latitude ranges greater than about 50 degrees, and that earlier support drew on
hemisphere-biased samples. Wells (2012) reported that the cline may run through fat rather than lean
mass, with Polynesian populations contradicting every trend. Savell, Auerbach and Roseman (2016) used
quantitative genetic modelling to show that some limb clines are correlated side effects rather than
adaptations, and concluded that group mean differences are poor evidence of adaptation. Riemer, Guralnick and White (2018) found no consistent mass-temperature relationship across endotherms
generally, in a sample of 952 bird and mammal species.</p>

<h2>Climate and size in the fossil record</h2>

<p>Three analyses bear directly on this, and they were built differently enough that the places they
converge are worth as much as the places they do not.</p>

<p><a href="papers/{P['stibel2023body']['slug']}.html">Stibel (2023b)</a> tested five paleoclimate
records against body size in 247 <em>Homo</em> specimens across 700,000 years. Body mass averages 66.40 kg in cooler periods against 59.00 kg in warmer ones, a difference
the paper reports as 11.8 percent, with proportions shifting toward more linear builds in heat.
Stature alone shows no significant difference.</p>

<p><a href="papers/{P['stibel2023climate']['slug']}.html">Stibel (2023a)</a> ran the equivalent test
on cranial capacity in 298 <em>Homo</em> specimens over 50,000 years. Brain size correlates inversely with temperature at r = &minus;0.362, holding after
controls for geography, sex and taxon. Cooler-period specimens average 1,426 g against 1,281 g in
warmer periods, a difference the paper reports as 10.7 percent. The signal appears to begin roughly 15,000 years ago. Humidity is
a weaker predictor and precipitation is not significant.</p>

<p><a href="papers/{P['will2021']['slug']}.html">Will et al. (2021)</a> tested a wider set of
environmental variables across a million years.
They found temperature a major predictor of body size, consistent with both analyses above. For brain
size they found net primary productivity and long-term precipitation variability correlated, but
explaining low amounts of variance, and concluded most environmental variables do not correspond with
brain size evolution.</p>

<p>All three agree temperature predicts body size, and the two body size estimates are close. Where
they part is whether brain size carries an independent climate signal or follows body size down. That
distinction matters, because Ruff, Trinkaus and Holliday (1997) showed that endocranial trends cannot
be read without a matched body mass series. Stibel (2023a) is explicit that its data can only provide correlational support, and that it is unclear whether brain size was selected on directly or drifted
alongside body size.</p>

<h2>Does current warming shrink brains?</h2>

<p>No such claim is established, although several news outlets have conflated the finding in that
direction. The signal at issue spans hundreds of generations, and it describes selection on
populations, not a response an individual body makes to a warm decade.</p>

<p>Two things work against reading it forward. The first is that clothing, shelter and heating
decouple modern bodies from ambient temperature, which is why Katzmarzyk and Leonard found the
climate-body slopes had flattened since Roberts measured them, and why Stibel (2023b) argues cultural adaptation muted the morphological response in later periods. The second is that
modern cranial dimensions do move on short timescales, as Jantz and Jantz (2016) have documented, but
through nutrition, disease burden and growth conditions rather than temperature, and the measured
direction is upward.</p>

<h3>Sources on this page</h3>
{sources(['stibel2023climate', 'stibel2023body', 'will2021', 'roberts1953', 'ruff1994', 'katzmarzyk1998', 'foster2013', 'wells2012', 'savell2016', 'riemer2018', 'ruff1997', 'jantz2016'])}
"""
    return write("climate.html", shell("climate.html", "Climate, body size and brain size", d, body,
                                       [article_ld("Climate, body size and brain size", d, "climate.html")]))


# =========================================================== 5. BODY SIZE
def page_body():
    d = ("Brains scale with bodies, so any claim about brain size reduction has to account for body "
         "size change over the same period. Several analyses suggest much of it does.")
    body = f"""
<h1>Body size and allometry</h1>

<div class="answer">
<p><strong>A brain that shrinks in proportion to its body has not changed in any interesting
way.</strong> Body mass fell over the same period cranial capacity did. Controlled for lean body
mass, the change in encephalization looks isometric, which suggests much of the apparent modern
decline reflects rising body fat rather than lost neural tissue.</p>
</div>

<h2>Why this comes first</h2>

<p>Brain mass scales predictably with body mass across mammals. Ruff, Trinkaus and Holliday made the
point directly in <em>Nature</em> in 1997: endocranial volume trends in Pleistocene <em>Homo</em>
cannot be interpreted without a matched body mass series, because body size was changing too. It is
the standard objection to any brain size claim, and it applies to all sides of the current dispute.</p>

<h2>The isometry result</h2>

<p><a href="papers/{P['stibel2021']['slug']}.html">Stibel (2021)</a> addresses this question directly,
using matched cranial and postcranial remains to compute encephalization rather than inferring it. The modern sample comes out 17% less encephalized than the <em>H. sapiens</em>
comparison. But controlled for <strong>lean</strong> body mass the change becomes isometric.</p>

<p>The implication is counterintuitive. Much of the apparent decline in modern encephalization may be
an artefact of obesity inflating the body mass denominator, not a reduction in neural tissue. The
modern sample's mean BMI is 25.3, in the overweight range, and BMI correlates with encephalization
quotient at r = 0.84 within that sample. The brain-body relationship that holds across earlier groups
(r = 0.66 for Plio-Pleistocene hominins, 0.82 for the Late Pleistocene, 0.43 for the Early Holocene)
collapses entirely in the modern sample at r = 0.08.</p>

<div class="note"><span class="lbl">Sample caution</span>
<p>The modern comparison rests on autopsy data from 19 individuals, 11 German and 8 Australian
Aboriginal males, all deceased between 1980 and 1982. That is a narrow basis for a claim about modern
humans generally, and it limits how far the isometry result can be pushed.</p></div>

<h2>Body shape, not just mass</h2>

<p><a href="papers/{P['stibel2023body']['slug']}.html">Stibel (2023b)</a> extends this to proportion
across 87 specimens. Stature-to-body-mass ratio is 7.09% greater in warmer cycles, rising to 9.89% at
10,000-year averaging: more linear builds in heat, stockier in cold. Stature itself shows no
significant difference across temperature cycles.</p>

<p>The paper is candid about the weaknesses here. The proportionality sample is small and skewed
toward high-latitude males, testing proportionality is "approximate at best," results using the
Ponderal Index were not significant, and the shape effect may be an artefact of the strong body mass
effect. The finding is also flagged as having a taxonomic implication: because morphology is used to
classify within <em>Homo</em>, some species boundaries may partly reflect climatic period.</p>

<p>That last point has independent support. Will and Stock (2015) found no simple geographic or
chronological trend in early <em>Homo</em> body size across 39 postcranial specimens, and Monson, Weitz and Brasil (2026) found <em>H. floresiensis</em> and <em>H. naledi</em> endocranial volumes fall where their
body sizes predict given the <em>Homo</em> scaling relationship, rather than being anomalously small.</p>

<h2>What is left to explain</h2>

<p>If a substantial share of measured brain decline is allometric, the residual needing a cognitive or
cultural explanation is smaller than headline figures imply. Climate models account for a minority of
variance in both Stibel's and Will's analyses. A large fraction of the variation in human brain size
remains unexplained by any published mechanism, which is the gap the
<a href="cognitive-offloading.html">offloading</a> and
<a href="self-domestication.html">self-domestication</a> arguments try to fill.</p>

<h3>Sources on this page</h3>
{sources(['stibel2021', 'stibel2023body', 'will2021', 'willstock2016', 'ruff1997', 'ruff1994', 'monson2026', 'smaers2021', 'deaner2007'])}
"""
    return write("body-size.html", shell("body-size.html", "Body size and allometry", d, body,
                                         [article_ld("Body size and allometry", d, "body-size.html")]))


# =========================================================== 6. COGNITION
def page_cognition():
    d = ("Brain volume and measured intelligence correlate weakly within living humans, and the size "
         "of that correlation is itself disputed. What the evidence supports, and what it does not.")
    body = f"""
<h1>Brain size and cognitive ability</h1>

<div class="answer">
<p><strong>The correlation is real, weak, and contested in both directions.</strong> Pooled estimates
run from r = .24 (Pietschnig et al. 2015, 88 studies) to r = .31 (Gignac and Bates 2017,
reanalysing the same data), with the largest single study, Nave et al. (2019) at n = 13,608, giving r = .19. All of them leave
most variance unexplained. Neanderthals had larger brains than living humans, and measured cognitive
performance rose sharply through the twentieth century.</p>
</div>

<h2>How large is the association</h2>

<p>Pietschnig et al. (2015) pooled 88 studies covering more than 8,000 individuals in 2015 and found
r = .24, about 6% of variance. They reported that null results had been systematically omitted and
that effect sizes had declined over time, concluding it "is not warranted to interpret brain size as
an isomorphic proxy of human intelligence differences."</p>

<p>Gignac and Bates (2017) reanalysed that same dataset and reached a different answer.
Restricting to healthy adults and accounting for the quality of the intelligence measure, they found
r = .31, rising to .39 for studies using excellent measures, and argued the true value is closer to
.40 with no detectable publication bias. The disagreement is live and unresolved.</p>

<p>The largest single study, Nave et al.'s (2019) preregistered analysis of 13,608 UK Biobank
participants, found r = .19 for fluid intelligence after controlling for sex, age, height,
socioeconomic status and population structure. Around 2% of variance.</p>

<p>Whichever figure is closer, the same conclusion follows for this topic: a population-level change
in average cranial capacity of a few percent cannot be converted into a claim about cognitive
capacity. The relationship is too weak and the confounds too large.</p>

<h2>Volume is the wrong variable</h2>

<p>A substantial literature argues that gross size is simply a poor measure. Logan et al. (2018) set out the case: volume conflates independently evolving components, and organisation,
connectivity and neuron density carry the explanatory weight. Deaner et al. (2007) found that overall
brain size, not encephalization quotient, best predicts cognitive ability across non-human primates,
undercutting the standard comparative currency. Smaers et al. (2021) showed across roughly 1,400
mammals that brain-body scaling slopes vary by clade and over time, so one encephalization formula is
not comparable across lineages.</p>

<p>Herculano-Houzel's (2009) cell-counting work reframed the question again: the human brain is a linearly
scaled-up primate brain, and neuron number rather than volume is the quantity that tracks capability.</p>

<p>Neubauer, Hublin and Gunz (2018) applied this directly to human evolution. Endocranial volume was already
within the modern range 300,000 years ago; what changed afterwards was shape, becoming globular
between roughly 100,000 and 35,000 years ago. Ponce de León et al. (2021) similarly found that
ape-like frontal organisation persisted long after the genus <em>Homo</em> originated, separating
reorganisation from enlargement.</p>

<h2>Three facts that complicate any simple story</h2>

<ul>
<li><strong>Neanderthals had larger brains.</strong> Würm-period Neanderthal cranial capacity averages
1,459 cc, statistically indistinguishable from contemporaneous <em>H. sapiens</em> and larger than the
modern average. Pearce, Stringer and Dunbar (2013) argue more of that volume went to vision and body control,
which is itself an argument that volume does not translate directly into general cognition.</li>
<li><strong>Measured performance rose while cranial capacity is argued to have fallen.</strong> Trahan
et al. (2014) put the Flynn effect at roughly 2.9 to 3 IQ points per decade across 285 studies from
1951 to 2010.</li>
<li><strong>That rise was environmental.</strong> Bratsberg and Rogeberg (2018) recovered the Flynn effect,
its turning point and its subsequent reversal entirely from within-family variation in Norwegian
conscript data, leaving no room for a genetic or biological explanation.</li>
</ul>

<h2>The genetic evidence, and its limits</h2>

<p><a href="papers/{P['stibel2021']['slug']}.html">Stibel (2021)</a> includes a review of
genome-wide association studies reporting small negative selection signals on cognition-associated
variants: estimated declines of 0.038 to 0.30 IQ points per decade, and roughly 1.5 months less
education per generation.</p>

<div class="note"><span class="lbl">Handle with care</span>
<p>These effects are small, and the paper states that the available genome datasets are "limited to
western cultures and not representative of the global population." They are also an order of magnitude
smaller than the Flynn effect running the other way over the same period, and Bratsberg and Rogeberg's
within-family analysis argues against a genetic reading of population cognitive change altogether.
Educational attainment is a social variable being used as a genetic proxy, which is a known weakness
in this literature.</p></div>

<h2>What the same paper says about its own proxy</h2>

<p>Stibel writes: "The link between brain size and cognitive ability is spurious at best, but the
relationship appears to hold strong validity when looked at with regards to evolutionary changes
within species." The first clause is frequently quoted alone, which makes the paper appear to dismiss
the link entirely. Both clauses matter, and the qualification is the part that applies here.</p>

<p>Encephalization is used across this literature because it is what fossils preserve, while the same
papers acknowledge it omits nearly everything that determines cognitive capacity: neuron count,
neuronal density, interneuron distance, axonal conduction velocity and cortical scaling.</p>

<h3>Sources on this page</h3>
{sources(['stibel2021', 'desilva2023', 'pietschnig2015', 'gignac2017', 'nave2019', 'logan2018', 'deaner2007', 'smaers2021', 'herculano2009', 'neubauer2018', 'poncedeleon2021', 'pearce2013', 'trahan2014', 'bratsberg2018'])}
"""
    return write("cognition.html", shell("cognition.html", "Brain size and cognitive ability", d, body,
                                         [article_ld("Brain size and cognitive ability", d, "cognition.html")]))


# =========================================================== 7. OFFLOADING
def page_offload():
    d = ("If information can be stored outside the head, the selective advantage of carrying more "
         "neural tissue weakens. The archaeological chronology, the experimental evidence, and the "
         "replication problems in it.")
    body = f"""
<h1>Cognitive offloading</h1>

<div class="answer">
<p><strong>Storing information outside the brain changes what the brain has to do.</strong> Symbols,
writing, tools and other people all hold what memory would otherwise carry. The argument that this
relaxed selection for larger brains rests on
<a href="papers/{P['stibel2025']['slug']}.html">Stibel (2025)</a>, which dates the end of brain
expansion to roughly 300,000 years ago and sets it against the archaeological record of external
information storage. It is an interpretation consistent with the chronology rather than a directly
tested cause, and the paper says so.</p>
</div>

<h2>Where the argument starts</h2>

<p><a href="papers/{P['stibel2025']['slug']}.html">Stibel (2025)</a>, in <em>Brain and Cognition</em>,
assembles 800 cranial capacity measurements across the genus <em>Homo</em> and asks a different
question from the rest of this literature. Not why brains shrank recently, but why they stopped
growing at all.</p>

<p>The answer it finds is that expansion ends around 300,000 years ago. There is no significant growth
trend after that point (Kruskal-Wallis <em>H</em> = 135.08, <em>p</em> &lt; 0.0001 across bins), and
factorial ANOVA finds significant effects of time (<em>F</em> = 208.22), climate stage
(<em>F</em> = 44.73) and their interaction (<em>F</em> = 5.17), all at <em>p</em> &lt; 0.0001. The
proposed reading is that directional selection for expansion gave way to stabilising selection.</p>

<p>Something else changes at the same boundary. Glacial-interglacial differences in brain size appear
only in the last 100,000 years (<em>p</em> &lt; 0.0001); between 100,000 and 300,000 years ago there
is no such difference (<em>p</em> = 0.923). Populations that had been indifferent to climate stage
became sensitive to it, which is what you would expect if brains had reached a size where their
energetic cost had started to bite. The paper puts that cost at roughly 20 percent of adult resting
energy consumption and up to 60 percent in early development.</p>

<h3>Why cost is the pivot</h3>

<p>A large brain has to earn what it consumes, and several independent literatures establish how
expensive that is. Kuzawa et al. (2014) measured childhood brain glucose use at 66.3 percent of
resting metabolic rate in males and 65.0 percent in females, and found body growth slows as brain
demand rises. Fonseca-Azevedo and Herculano-Houzel (2012) identified a feeding-time ceiling on how
many neurons a primate can support at a given body size. Aiello and Wheeler's (1995) expensive tissue hypothesis proposed the brain was paid for by a reduced gut, though Navarrete et al. (2011) later
found no such trade-off across a large mammal sample once fat was accounted for, and Pontzer et al.
(2016) showed humans expanded the total energy budget rather than only reallocating within it. Isler
and van Schaik's (2009) expensive brain framework treats size as jointly limited by energy supply and
by allocation away from growth and reproduction.</p>

<h3>The chronological overlap</h3>

<p>The plateau is where the offloading argument enters. Stibel (2025) sets the date of the plateau
against the archaeological record of information held outside the head.</p>

<table>
<tr><th>Date</th><th>Evidence</th></tr>
<tr><td>~430,000 years ago</td><td>Anatomical features associated with vocalisation and auditory
sensitivity appear</td></tr>
<tr><td>~300,000 years ago</td><td>Brain size growth plateaus</td></tr>
<tr><td>~142,000&ndash;100,000</td><td>Shell beads, Bizmoune Cave</td></tr>
<tr><td>~100,000&ndash;75,000</td><td>Engraved ochre, Blombos Cave</td></tr>
<tr><td>~65,000</td><td>Engraved ostrich eggshell, Diepkloof Rock Shelter</td></tr>
<tr><td>~50,000</td><td>Bones marked with systematic notation</td></tr>
<tr><td>~40,000</td><td>Substantial elaboration of symbolic material culture</td></tr>
</table>

<p>The paper is careful about what this shows. It points "not to a sudden cognitive revolution, but to
cumulative cultural evolution," and it states plainly that the offloading account is an interpretation
consistent with the chronology rather than a directly tested causal result. Its other stated limits
are that the trend "is not strictly monotonic and should be interpreted cautiously," that finer
temporal bins lacked the sample sizes for robust glacial-interglacial comparison, and that low sample
sizes within <em>Homo</em> required model-free curve fitting and coarse binning. Taxonomically
contested specimens (<em>H. floresiensis</em>, <em>H. naledi</em>) were tested in and out without
changing the direction or significance of the result.</p>

<p>Muthukrishna and Henrich (2016) give the mechanism a formal treatment, arguing innovation rate is a
property of population size, interconnectedness and transmission fidelity rather than individual
intelligence. On that account collective capability can rise while individual neural capacity stays
flat or falls, which is the shape Stibel's data show.</p>

<p>Two findings complicate the timing. Neubauer et al. (2018) report that endocranial volume was
already modern at 300,000 years and only shape changed afterwards, which would make the plateau the
start of a reorganisation rather than a ceiling. Du et al. (2018) separately showed that conclusions
about the pace of hominin brain size change are sensitive to how the data are binned, an objection
that applies to the coarse bins Stibel's sample sizes required.</p>

<h2>The modern experimental evidence</h2>

<p>Work on contemporary offloading is often cited as support. It is weaker than it looks, and a
resource that leans on it should say so.</p>

<p>Risko and Gilbert (2016) define the field and frames offloading as adaptive metacognitive
strategy selection, not decline. Gilbert et al. (2020) later showed offloading is governed by
metacognitive confidence rather than actual memory ability, with people systematically over-offloading:
a rational-but-biased decision rather than erosion of capacity.</p>

<p>Sparrow, Liu and Wegner's (2011) "Google effects on memory" is the most-cited experimental basis for the
idea that search changes memory. It is also among the least replicated. Hesselmann's (2020) preregistered direct replication did not reproduce the effect. Ward et al.'s (2017) "brain drain" finding,
that a nearby smartphone reduces working memory, likewise failed to replicate in Ruiz Pardo and Minda's (2022) preregistered study. Two meta-analyses of the brain drain literature reach opposite
conclusions: Parry (2023) finds null effects for most cognitive functions; Böttger et al. (2023) find the effect real.</p>

<p>Where the evidence is cleaner, it shows reallocation rather than loss. Grinschgl et al. (2021) found offloading improves immediate performance and worsens later memory for the offloaded content
specifically. Storm and Stone (2015) found that saving one file before studying another <em>improves</em>
memory for the second. That is a cost-benefit structure, not a decline.</p>

<h2>Related but distinct ideas</h2>

<ul>
<li>Clark and Chalmers' (1998) <strong>extended mind</strong> is a philosophical claim that cognitive
processes can literally extend into the environment. Sterelny's (2010) <strong>scaffolded mind</strong>
accounts for the same evidence without the metaphysical commitment, and is the main sceptical
alternative.</li>
<li>Malafouris's (2019) <strong>material engagement theory</strong> treats things as participating in
cognition rather than merely recording it.</li>
<li><strong>Distributed cognition</strong> describes cognitive work spread across people and
artefacts, and is what DeSilva et al. (2021) invoked through the eusocial insect analogy.</li>
</ul>

<div class="note"><span class="lbl">What Stibel (2025) does not claim</span>
<p>It does not argue that tools, artefacts or machines possess intelligence or consciousness. The words
"consciousness" and "extended mind" do not appear in it. Artificial intelligence is mentioned once, as
a modern analogy, citing work on offloading to search engines and AI assistants. The argument concerns
selection pressure on human neuroanatomy.</p></div>

<h3>Sources on this page</h3>
{sources(['stibel2025', 'desilva2021', 'kuzawa2014', 'fonseca2012', 'aiello1995', 'navarrete2011', 'pontzer2016', 'isler2009', 'risko2016', 'sparrow2011', 'hesselmann2020', 'ward2017', 'ruizpardo2022', 'parry2023', 'bottger2023', 'grinschgl2021', 'storm2015', 'muthukrishna2016', 'clark1998', 'sterelny2010', 'malafouris2019', 'neubauer2018', 'du2018'])}
"""
    return write("cognitive-offloading.html",
                 shell("cognitive-offloading.html", "Cognitive offloading", d, body,
                       [article_ld("Cognitive offloading", d, "cognitive-offloading.html")]))


# =========================================================== 7b. SELF-DOMESTICATION
def page_selfdom():
    d = ("Domesticated mammals have smaller brains than their wild ancestors. Whether humans "
         "underwent an equivalent process is argued from craniofacial evidence and disputed.")
    body = f"""
<h1>Self-domestication</h1>

<div class="answer">
<p><strong>Across the domesticated eutherian lineages Kruska reviewed, brain size is reduced by
roughly 8 to 30 percent relative to wild ancestors.</strong> Humans show some of the same skeletal
changes over the same period their crania were reducing. Whether that
reflects an equivalent process, or a coincidence of separate causes, is actively disputed.</p>
</div>

<h2>The comparative baseline</h2>

<p>Kruska's (2005) review across eutherian mammals found brain size reductions of roughly 8 to 30 percent in
domesticated lineages, and, importantly, that returning animals to the wild does not restore wild-type
brain size. Balcarcel et al. (2021) found that the reduction in cattle scales with the intensity of human
contact, with dairy breeds most reduced and fighting bulls least.</p>

<p>Wilkins, Wrangham and Fitch (2014) proposed a developmental mechanism: mild neural crest cell
deficits, selected for indirectly through tameness, produce the whole domestication syndrome including
smaller brains, shorter faces and reduced pigmentation.</p>

<h2>The human case</h2>

<p>Cieri et al. (2014) documented brow ridge reduction and upper facial shortening from the Middle
Pleistocene to recent humans, and argued this reflects selection for social tolerance. Hare's (2017) "survival of the friendliest" account develops the case that selection for prosociality drove a
domestication-like syndrome in <em>H. sapiens</em>. On this reading the cranial reduction of the last
tens of thousands of years is a by-product of becoming a more cooperative species, not a response to
climate or a consequence of offloading.</p>

<h2>Why it is contested</h2>

<p>Sánchez-Villagra and van Schaik (2019) reviewed the human application directly and concluded the
evidence that humans display the domestication trait set is weaker and more equivocal than the popular
framing suggests.</p>

<p>The underlying mechanism has also come under pressure. Johnsson, Henriksen and Wright (2021) argued that the neural crest hypothesis does not provide a unified explanation for domestication;
Wilkins, Wrangham and Fitch (2021) published a reply in the same issue. Lord et al. (2020) showed that the
Russian farm-fox experiment, the empirical keystone of the whole framework, used founders already bred
in captivity for decades, which undercuts its status as a clean demonstration. Gleeson and Wilson (2023) have proposed a third account based on shared reproductive disruption.</p>

<p>Leach (2003) offered an alternative that requires no domestication analogy at all: the dietary, activity
and shelter changes of sedentism are sufficient to produce gracilization, and those changes coincide
with the Holocene period in question.</p>

<h2>How it relates to the other explanations</h2>

<p>Self-domestication and cognitive offloading are not rivals in any strict sense. Both describe
selection relaxing on individually costly traits as social organisation takes on more of the load.
They differ in mechanism, one developmental and one cognitive, and in what evidence would settle them.
Neither is established, and both have to contend with the possibility that the reduction they explain
is smaller than reported, or absent.</p>

<h3>Sources on this page</h3>
{sources(['kruska2005', 'balcarcel2021', 'wilkins2014', 'johnsson2021', 'wilkins2021reply', 'lord2020', 'gleeson2023', 'cieri2014', 'hare2017', 'sanchez2019', 'leach2003'])}
"""
    return write("self-domestication.html",
                 shell("self-domestication.html", "Self-domestication", d, body,
                       [article_ld("Self-domestication", d, "self-domestication.html")]))


# =========================================================== 7c. SIZE RULES
def page_rules():
    d = ("Does Cope's rule apply to humans? Do Bergmann's and Allen's? Humans follow the two "
         "climate rules reasonably well and Cope's rule barely at all. What the hominin fossil "
         "record shows for each.")
    body = f"""
<h1>Do the biological rules apply to humans?</h1>

<div class="answer">
<p><strong>Two of the three hold up; the third does not.</strong> Bergmann's rule, that bodies are
larger in cold climates, and Allen's rule, that limbs are shorter, both describe human populations
reasonably well and have been tested against the fossil record. Cope's rule, that lineages grow
larger over time, fits the hominin record poorly. None of the three is about brain size.</p>
</div>

<h2>What the three rules say</h2>

<table>
<tr><th>Rule</th><th>Prediction</th><th>How well humans fit</th></tr>
<tr><td><strong>Bergmann's</strong></td><td>Body mass is greater in colder climates</td>
<td>Holds broadly, with real exceptions and a disputed mechanism</td></tr>
<tr><td><strong>Allen's</strong></td><td>Limbs and extremities are shorter in colder climates</td>
<td>Holds, and is arguably the better supported of the two</td></tr>
<tr><td><strong>Cope's</strong></td><td>Lineages increase in body size over evolutionary time</td>
<td>Poorly. Tested three times against hominins, with mixed results</td></tr>
</table>

<p>The first two are <em>ecogeographic</em>: they describe variation across space, between populations
living in different climates. Cope's rule is <em>temporal</em>: it describes change through time
within a lineage. They answer different questions, which is part of why they can disagree.</p>

<h2>Bergmann's rule</h2>

<p>Roberts (1953) established the basic relationship between body weight and mean annual temperature
across human populations, and it has been retested repeatedly since. Katzmarzyk and Leonard (1998)
restudied it across 418 samples and confirmed the association, while noting the slopes had grown
shallower since Roberts measured them, which they attributed to twentieth-century nutritional change.
Ruff's (1994) review remains the standard treatment, and identified body <em>breadth</em> rather than
stature as the dimension climate actually constrains.</p>

<p>It is less firm than its textbook status suggests. Foster and Collard (2013) found it holds in
humans only across latitude ranges greater than about 50 degrees, and that earlier support drew on
hemisphere-biased samples. Wells (2012) argued the cline may run through fat rather than lean mass,
with Polynesian populations contradicting every trend. Savell, Auerbach and Roseman (2016) used
quantitative genetic modelling to show some limb clines are correlated side effects rather than
adaptations. And Riemer, Guralnick and White (2018) found no consistent mass-temperature relationship
across 952 bird and mammal species, which challenges the rule as a general law rather than a local
pattern.</p>

<h2>Allen's rule</h2>

<p>Allen's rule concerns proportion rather than mass: shorter limbs and extremities reduce surface
area relative to volume, conserving heat. In humans it shows up as relative sitting height, limb
length and trunk breadth varying with latitude, and it survives scrutiny somewhat better than
Bergmann's because proportion is less confounded by nutrition than mass is.</p>

<p><a href="papers/{P['stibel2023body']['slug']}.html">Stibel (2023b)</a> tested both rules against
deep time rather than across living populations. Across 247 <em>Homo</em> specimens and 700,000
years, body mass in cooler periods averages 66.40 kg against 59.00 kg in warmer ones, and the
stature-to-body-mass ratio is 7.09% greater in warmer cycles, rising to 9.89% at 10,000-year
averaging. Stature alone shows no significant difference. That is the Bergmann and Allen pattern
holding through time, not just across space. The paper is candid that the proportionality sample is
small at 87 specimens and skewed toward high-latitude males, and that the shape effect may be an
artefact of the strong mass effect. <a href="climate.html">More on climate</a></p>

<h2>Cope's rule, and why it fits worst</h2>

<p>Cope's rule is the weakest of the three here. Will, Pablos and Stock (2017) assembled 254 body mass and 204 stature estimates from 311 specimens
spanning 4.4 million years and found a significant positive association between size and time, which
is what Cope's rule predicts. They qualified it heavily: phases of stasis punctuated by rapid
increases, a reduction among australopithecines between roughly 3.2 and 2.2 Ma, and clear exceptions
in <em>H. naledi</em>, <em>H. floresiensis</em> and declining Holocene <em>H. sapiens</em>. Gardner,
Püschel, White, Sakamoto and Venditti (2026) revisited it with 386 specimens across 21 taxa and found
strong evidence for body mass increase in later <em>Homo</em> and moderate support for a general
increase. A correction to that paper was published in August 2026.</p>

<p><a href="papers/{P['stibel2023body']['slug']}.html">Stibel (2023b)</a> reaches a different
conclusion. Body mass does increase over time (<em>p</em> &lt; 0.0001, ANOVA), but the trend is cubic
rather than directional, and the paper states that its results "do not support Cope's rule" because
<em>Homo</em> body size "has not consistently increased over time."</p>

<h3>The rule that reconciles them</h3>

<p>Hunt and Roy (2006) proposed a <strong>Cope-Bergmann rule</strong>: apparent size increase over
geological time is really a correlated response to time and temperature together, rather than a
directional trend in its own right. <a href="papers/{P['stibel2023body']['slug']}.html">Stibel (2023b)</a> finds support for that
reading, with models including both time and climate significant at <em>p</em> &lt; 0.0001 across the
same 247 specimens.</p>

<p>On that account the size increase is real, but Cope's rule is the wrong explanation for it. The
driver is climate, which is Bergmann's territory, rather than any general fitness advantage to being
larger. That is also why this page treats the three rules together rather than separately: for
humans, the interesting answer sits between them.</p>

<h2>None of this is about brain size</h2>

<p>All three rules concern the body. The hominin brain literature uses a different framework and asks
a different question: whether encephalization accumulated within lineages, or through the replacement
of smaller-brained species by larger-brained ones.</p>

<p>Püschel, Nicholson, Baker, Barton and Venditti (2024) answered that directly. Across 285 specimens
analysed over 1,000 Bayesian phylogenies they found a significant within-species effect of time on
relative brain size and no significant between-species effect, with speciation rate not a predictor.
Their conclusion is that hominin brain size macroevolution "seems to be entirely explained by
micro-evolutionary, population-level processes." The within-species trend accelerates in more recent
lineages, correlating with time position at r = 0.74, or 0.9 with Neanderthals excluded.</p>

<p>That is a finding about anagenesis versus cladogenesis. It is a related question, since both
concern whether change happens inside lineages or between them, but no published study frames hominin
brain size in Cope's rule terms and this page does not either. Montgomery, Capellini, Barton and Mundy
(2010) tested Cope's rule across primates and rejected it, treating brain size separately from body
size throughout.</p>

<h2>Scale changes the answer</h2>

<p>Du et al. (2018) showed that conclusions about the pace and pattern of hominin brain size change
are scale-dependent: how the data are binned substantially affects what trend appears. Gingerich
(2022) synthesised 14 studies into a single endocranial series and recovered four phases, stasis from
roughly 3.2 to 2.0 Ma, increase from 2.0 to 1.5 Ma, stasis from 1.5 to 0.7 Ma, and increase from
about 0.7 Ma onward. His median step rate of 0.15 standard deviations per generation is close to rates
measured in living populations, a useful check that the fossil rates are not anomalous.</p>

<p>Any claim that humans do or do not follow one of these rules has to specify the timescale first.</p>

<h3>Sources on this page</h3>
{sources(['roberts1953', 'ruff1994', 'katzmarzyk1998', 'foster2013', 'wells2012', 'savell2016', 'riemer2018', 'stibel2023body', 'willpablos2017', 'gardner2026', 'puschel2024', 'montgomery2010', 'gingerich2022', 'du2018', 'willstock2016'])}
"""
    return write("biological-rules.html",
                 shell("biological-rules.html",
                       "Bergmann's, Allen's and Cope's rules in humans",
                       d, body,
                       [article_ld("Do the biological rules apply to humans? "
                                   "Bergmann's, Allen's and Cope's rules", d, "biological-rules.html")]))


# =========================================================== 8. QUESTIONS
def _pl(key, label=None):
    """Inline link to a paper page, for use inside Q&A answers."""
    p = P[key]
    return f'<a href="papers/{p["slug"]}.html">{label or (p["author_short"] + " (" + yr(key) + ")")}</a>'


QAS = [
 ("Has the human brain gotten smaller?",
  f"<p>Over evolutionary time, most published studies say yes. Brain size expanded through the "
  f"Pleistocene, stopped growing around 300,000 years ago ({_pl('stibel2025')}), and declined during "
  f"the Holocene. {_pl('desilva2023')} report that across 19 studies spanning about 90 years, the "
  f"average decrease since the Late Pleistocene is 8.5%. {_pl('villmoare2022')} found no detectable "
  f"reduction in a reanalysis, and that paper has not been withdrawn. The disagreement is "
  f"methodological, centring on whether crania from different populations and periods can be "
  f"pooled.</p>"),
 ("When did the human brain start shrinking?",
  f"<p>{_pl('desilva2021')} used change-point analysis to place it around 3,000 years ago. After "
  f"criticism from {_pl('villmoare2022')}, {_pl('desilva2023')} widened this to roughly 5,000–3,000 "
  f"years BP and conceded the timing is uncertain. {_pl('stibel2023climate')}, working from "
  f"paleoclimate records rather than change-point analysis, finds a response beginning around 15,000 "
  f"years ago. Henneberg (1988) dated decreasing skull size to the broader Holocene.</p>"),
 ("How much smaller is the modern human brain?",
  f"<p>Estimates cluster around a 100–150 cc reduction from Late Pleistocene values, or roughly 5–10% "
  f"depending on the comparison period and reference dataset. {_pl('desilva2023')} give Pleistocene "
  f"<em>H. sapiens</em> at about 1,458 cc against modern weighted averages of 1,308 to 1,392 cc, and "
  f"frame the change as about one standard deviation over 10,000 years. {_pl('stibel2021')}, using "
  f"matched cranial and postcranial remains, puts the reduction at 5.4% relative to the Upper "
  f"Palaeolithic.</p>"),
 ("Why is the human brain shrinking?",
  f"<p>No single cause is established, and four explanations are actively argued without being "
  f"mutually exclusive. Body size decline, with brains scaling allometrically ({_pl('stibel2021')}). "
  f"Climate, with warming periods correlating with smaller size ({_pl('stibel2023climate')}). A "
  f"metabolic ceiling making very large brains too costly ({_pl('stibel2025')}). And cognitive "
  f"offloading onto tools, symbols and social groups reducing selection for larger brains "
  f"({_pl('desilva2021')}; {_pl('stibel2025')}). Self-domestication is a fifth account, argued from "
  f"craniofacial evidence by Cieri et al. (2014).</p>"),
 ("Does a smaller brain mean we are less intelligent?",
  f"<p>No. Within living humans the relationship between brain volume and measured intelligence is "
  f"weak: Pietschnig et al. (2015) put it at r = .24 across 88 studies, Gignac and Bates (2017) "
  f"reanalysed the same data and argued for r ≈ .40, and Nave et al. (2019) found r = .19 in 13,608 "
  f"UK Biobank participants. Neanderthals had larger brains than living humans "
  f"({_pl('desilva2023')}). Measured cognitive performance rose roughly 3 IQ points per decade "
  f"through the twentieth century (Trahan et al. 2014), and Bratsberg and Rogeberg (2018) showed that "
  f"rise was environmental. See {_pl('stibel2021')} for the author's own statement of what the proxy "
  f"can and cannot support.</p>"),
 ("Is climate change making human brains smaller?",
  f"<p>Not in any sense that applies to people alive today. {_pl('stibel2023climate')} finds brain "
  f"size averaging about 10.7% lower during warm periods across a 50,000-year record, and notes the "
  f"response may persist. That is a claim about a multi-millennial evolutionary signal spanning "
  f"hundreds of generations, not a prediction about individuals. Clothing, shelter and heating also "
  f"decouple modern bodies from ambient temperature, and Katzmarzyk and Leonard (1998) found the "
  f"climate-body relationship measured across living populations had flattened over the twentieth "
  f"century for that reason. Headlines saying current warming is shrinking our brains outrun the "
  f"evidence.</p>"),
 ("Did human brains shrink because of agriculture or civilisation?",
  f"<p>This was the proposal in {_pl('desilva2021')}: that complex societies allowed knowledge to be "
  f"held collectively rather than individually, reducing selection for large individual brains, by "
  f"analogy with eusocial ant colonies. It is the specific hypothesis {_pl('villmoare2022')} "
  f"challenged. It remains a live idea but is not established.</p>"),
 ("Was the brain shrinkage claim debunked?",
  f"<p>No, though search results give that impression. {_pl('desilva2021')} was challenged by "
  f"{_pl('villmoare2022')}, which found no reduction, and answered by {_pl('desilva2023')}, which "
  f"conceded sampling problems while maintaining a statistically significant decline across corrected "
  f"datasets. {_pl('decaro2024')} continued the exchange. Neither position has been withdrawn.</p>"),
 ("Is the human brain still shrinking today?",
  f"<p>Unknown, and the question is harder than it sounds because two different things get called the "
  f"same trend. {_pl('stibel2021')} reports the encephalization trend over the past thousand years "
  f"running negative (r = −0.483) against a positive prehistoric trend (r = 0.777). Over the past "
  f"century, by contrast, directly measured brain weight and intracranial volume have been rising "
  f"(Miller and Corsellis 1977; DeCarli et al. 2024). Those measurements are separated by only a few "
  f"generations, which is too short for selection, so they describe growth conditions rather than "
  f"evolution.</p>"),
 ("Are human brains actually getting bigger now?",
  f"<p>In absolute terms, in directly measured modern samples, yes. Miller and Corsellis (1977) found "
  f"brain weight rising across the twentieth century in an autopsy series, and DeCarli et al. (2024) "
  f"found intracranial and cerebral volumes increasing across birth decades in Framingham Heart Study "
  f"participants born between 1930 and 1970.</p>"
  f"<p>Relative to body size, the picture reverses, and that is the measure that matters for "
  f"evolution. {_pl('stibel2021')} finds the modern sample 17% less encephalized than its "
  f"<em>H. sapiens</em> comparison. Bodies have grown faster than brains: mean BMI in that sample is "
  f"25.3, and the brain-to-body relationship that holds across earlier groups (r = 0.66 for "
  f"Plio-Pleistocene hominins, 0.82 for the Late Pleistocene) collapses to r = 0.08 in modern humans. "
  f"So brains are getting bigger in absolute terms while bodies grow faster still, not bigger "
  f"relative to those bodies. This is also a secular trend of the same kind that raised average "
  f"height, driven by nutrition, reduced childhood disease and better prenatal health, which makes it "
  f"developmental plasticity rather than evolutionary change.</p>"),
 ("Does obesity affect these measurements?",
  f"<p>Substantially, and this is one of the more surprising findings in {_pl('stibel2021')}. "
  f"Controlling for lean body mass rather than total body mass, encephalization change becomes "
  f"isometric, implying much of the apparent modern decline reflects increased body fat inflating the "
  f"denominator rather than lost neural tissue. In that sample BMI correlates with encephalization "
  f"quotient at r = 0.84, and the brain-to-body relationship that holds across earlier hominins breaks "
  f"down entirely.</p>"),
 ("When did human brains stop growing?",
  f"<p>Around 300,000 years ago. {_pl('stibel2025')} analysed 800 cranial measurements across the "
  f"genus <em>Homo</em> and found no significant growth trend after that point. This shifts the "
  f"question from why brains recently shrank to why a long expansion stopped, with metabolic ceilings "
  f"and cognitive offloading offered as explanations. Neubauer et al. (2018) reach a compatible "
  f"conclusion by a different route, finding endocranial volume already within the modern range at "
  f"300,000 years with only shape changing afterwards.</p>"),
 ("How large is the human brain compared to other hominins?",
  f"<p>{_pl('desilva2023')} give Late Pleistocene <em>H. sapiens</em> at about 1,458 ± 140 cc, "
  f"effectively identical to contemporaneous Würm-period Neanderthals at about 1,459 ± 182 cc. Modern "
  f"humans average roughly 1,345 cc. Earlier species were considerably smaller. Absolute size across "
  f"these groups is a poor guide to cognitive capability; Pearce, Stringer and Dunbar (2013) argue "
  f"more of the Neanderthal volume went to vision and body control.</p>"),
 ("Does Cope's rule apply to humans?",
  f"<p>Poorly, and it is the weakest of the three general biological rules as applied to humans. Cope's "
  f"rule predicts that lineages grow larger over evolutionary time. Will, Pablos and Stock (2017) "
  f"found a significant positive association between hominin body size and time but qualified it "
  f"heavily, and {_pl('stibel2023body')} found the trend cubic rather than directional and stated "
  f"its results do not support the rule. Bergmann's and Allen's rules, which concern climate rather "
  f"than time, fit humans considerably better. None of the three is about brain size. "
  f"<a href=\"biological-rules.html\">More on the biological rules</a></p>"),
 ("What is cognitive offloading?",
  f"<p>Storing or processing information outside the brain, in symbols, writing, tools, other people, "
  f"or now digital systems. Risko and Gilbert (2016) define the field. In this literature it is "
  f"proposed as a reason brain expansion stopped: if knowledge can be held externally, individual "
  f"neural capacity becomes less decisive, weakening selection for larger brains. "
  f"{_pl('stibel2025')} sets the archaeological chronology of external information storage against "
  f"the date the expansion ended.</p>"),
 ("Do these studies claim tools or AI are conscious?",
  f"<p>No. The {_pl('stibel2025', 'Stibel (2025) paper')} on brain size and extinction risk does not "
  f"mention consciousness, machine intelligence or the extended mind thesis. Artificial intelligence "
  f"appears once, as a modern analogy for offloading, citing research on how search engines and AI "
  f"assistants affect memory and attention. The argument concerns selection pressure on human "
  f"neuroanatomy.</p>"),
 ("Did human bodies get smaller too?",
  f"<p>Yes, and this matters for interpreting brain data. {_pl('stibel2023body')} finds that across "
  f"247 specimens and 700,000 years, body mass in warmer periods is lower by a margin the paper "
  f"reports as 11.8%. Body "
  f"proportions shift as well, toward more linear builds in heat. Stature specifically shows no "
  f"significant climate response, so the effect is on mass and shape rather than height. "
  f"{_pl('will2021')} independently found temperature a major predictor of body size across a million "
  f"years.</p>"),
 ("What would settle this question?",
  f"<p>More Holocene cranial samples, better geographic coverage outside Europe, and consistent "
  f"measurement methods across datasets. Both sides of the dispute explicitly call for this. "
  f"{_pl('desilva2023')} states directly that more samples from this period will be valuable, and "
  f"that timing and cause both warrant continued investigation.</p>"),
]

def page_questions():
    d = ("Direct answers to eighteen common questions about human brain size, evolution, climate and "
         "cognition, each sourced to the primary literature.")
    qa_html = "".join(f'<div class="qa"><h3>{html.escape(q)}</h3>{a}</div>' for q, a in QAS)
    keys = ["desilva2021", "villmoare2022", "desilva2023", "decaro2024", "stibel2021",
            "stibel2023climate", "stibel2023body", "stibel2025", "will2021",
            "henneberg1988", "hennebergsteyn1993", "ruff1997", "neubauer2018",
            "pietschnig2015", "gignac2017", "nave2019", "trahan2014", "bratsberg2018",
            "pearce2013", "risko2016", "cieri2014", "katzmarzyk1998",
            "miller1977", "jantz2016", "decarli2024"]
    body = f"""
<h1>Questions and answers</h1>
{qa_html}
<h3>Sources on this page</h3>
{sources(keys)}
"""
    return write("questions.html", shell("questions.html", "Questions and answers", d, body,
                                         [article_ld("Questions and answers", d, "questions.html"), faq_ld(QAS)]))


# =========================================================== 9. PAPERS
def page_papers():
    d = "Every study cited across this resource, grouped by what it bears on."
    EXCH  = ["desilva2021", "villmoare2022", "desilva2023", "decaro2024"]
    MECH  = ["stibel2021", "stibel2023climate", "stibel2023body", "stibel2025",
             "will2021", "henneberg1988", "hawks2011"]
    WIDER = []
    exch  = "".join(paper_card(k) for k in EXCH)
    mech  = "".join(paper_card(k) for k in MECH)

    def block(title, keys):
        return f"<h3>{title}</h3>" + sources(keys, note=True)

    body = f"""
<h1>Sources</h1>

<h2>The Holocene dispute</h2>
<p>Four papers published in <em>Frontiers in Ecology and Evolution</em> between 2021 and 2024.</p>
{exch}

<h2>Mechanism and measurement</h2>
<p>Studies testing what might drive brain and body size change: allometry, climate, metabolic limits,
cultural transmission.</p>
{mech}

<h2>Full bibliography</h2>

{block("Holocene cranial change", ['henneberg1988', 'hennebergsteyn1993', 'henneberg1998', 'beals1984'])}
{block("Secular change in living populations", ['miller1977', 'jantz2016', 'decarli2024'])}
{block("Climate, latitude and body form", ['ruff1994', 'ruff1997', 'katzmarzyk1998', 'foster2013', 'wells2012', 'savell2016'])}
{block("Brain energetics", ['aiello1995', 'navarrete2011', 'fonseca2012', 'kuzawa2014', 'pontzer2016', 'isler2009'])}
{block("Brain size and cognition", ['pietschnig2015', 'gignac2017', 'nave2019', 'logan2018', 'deaner2007', 'smaers2021', 'herculano2009', 'trahan2014', 'bratsberg2018'])}
{block("Cognitive offloading and distributed cognition", ['risko2016', 'sparrow2011', 'hesselmann2020', 'ward2017', 'ruizpardo2022', 'parry2023', 'bottger2023', 'grinschgl2021', 'storm2015', 'muthukrishna2016', 'clark1998', 'sterelny2010', 'malafouris2019'])}
{block("Domestication and gracilization", ['kruska2005', 'wilkins2014', 'cieri2014', 'hare2017', 'sanchez2019', 'leach2003'])}
{block("Archaic and Neanderthal comparisons", ['neubauer2018', 'poncedeleon2021', 'du2018', 'pearce2013', 'monson2026'])}

<h2>Further reading in the popular press</h2>

<p class="meta">Secondary sources. Everything above is the primary literature; these are accounts
written for a general reader. Coverage of both positions is listed, because a reader who has arrived
here from one of them should be able to find the other.</p>

<h3>Reporting on the decline and its causes</h3>
<ul class="lit">
<li><a href="https://www.wsj.com/science/human-brains-shrinking-evolution-science-980c45e">Our Big
Brains Have Shrunk. Scientists Might Know Why.</a> <em>The Wall Street Journal</em>, September 2023.
Covers the DeSilva et al. work and the exchange around it.</li>
<li><a href="https://www.bbc.com/future/article/20240517-the-human-brain-has-been-shrinking-and-no-one-quite-knows-why">The
human brain has been shrinking and no one quite knows why</a>. Jasmin Fox-Skelly, <em>BBC
Future</em>, 17 May 2024. The most widely read account, and one of the few that treats the question
as genuinely open.</li>
<li><a href="https://www.livescience.com/archaeology/human-evolution/if-humans-are-getting-smarter-why-are-our-brains-shrinking">If
humans are getting smarter, why are our brains shrinking?</a> Owen Jarus, <em>Live Science</em>,
9 May 2026. The most balanced piece available, quoting researchers on both sides.</li>
<li><a href="https://www.zmescience.com/science/news-science/human-brain-shrinking/">Human brains may
have started shrinking thousands of years ago. Scientists still can't agree why.</a> Tibi Puiu,
<em>ZME Science</em>, 18 May 2026. The most complete lay treatment of the full 2021&ndash;2024
exchange.</li>
<li><a href="https://www.psypost.org/evolution-may-have-capped-human-brain-size-to-balance-energy-costs-and-survival/">Evolution
may have capped human brain size to balance energy costs and survival</a>. <em>PsyPost</em>,
24 August 2025. Covers the metabolic ceiling and offloading argument.</li>
<li><a href="https://www.psypost.org/new-research-links-climate-change-to-shrinking-brain-size-in-modern-humans/">New
research links climate change to shrinking brain size in modern humans</a>. <em>PsyPost</em>.
Covers the climate analysis. The headline overstates the finding, which concerns a multi-millennial
signal rather than modern individuals.</li>
</ul>

<h3>Reporting on the 2022 reanalysis</h3>
<ul class="lit">
<li><a href="https://www.unlv.edu/news/release/unlv-research-no-human-brain-did-not-shrink-3000-years-ago">No,
the human brain did not shrink 3,000 years ago</a>. University of Nevada, Las Vegas news release,
August 2022. The source of most coverage of Villmoare &amp; Grabowski (2022).</li>
<li><a href="https://www.advancedsciencenews.com/no-the-human-brain-did-not-shrink/">No, the human
brain did not shrink</a>. Victoria Corless, <em>Advanced Science News</em>, 18 August 2022.</li>
<li><a href="https://www.sciencedaily.com/releases/2022/08/220807102043.htm">Did the human brain
shrink 3,000 years ago?</a> <em>ScienceDaily</em>, August 2022.</li>
</ul>

<p class="meta">None of the three pieces above has been updated since the 2023 response was published,
which is a large part of why the public record on this question is out of date.</p>

<h3>On the modern increase</h3>
<ul class="lit">
<li><a href="https://www.scientificamerican.com/article/human-brains-may-be-getting-bigger/">Human
brains may be getting bigger</a>. <em>Scientific American</em>. Covers DeCarli et al. (2024). Read
alongside <a href="index.html">the overview page</a> on why a secular increase over decades and an
evolutionary decline over millennia are not in conflict.</li>
<li><a href="https://www.discovermagazine.com/the-sciences/if-modern-humans-are-so-smart-why-are-our-brains-shrinking">If
modern humans are so smart, why are our brains shrinking?</a> Kathleen McAuliffe,
<em>Discover</em>, 2011. The oldest widely read treatment, predating the current dispute.</li>
</ul>

<h2>Licence and access</h2>
<table>
<tr><th>Paper</th><th>Licence</th><th>Access</th></tr>
{"".join(f'<tr><td><a href="papers/{P[k]["slug"]}.html">{P[k]["author_short"]} {yr(k)}</a></td><td>{P[k]["license"]}</td><td>{P[k].get("oa","")}</td></tr>' for k in EXCH + MECH + WIDER)}
</table>
<p class="meta">Two studies carry CC BY-NC licences, which prohibit commercial reuse. This resource is
non-commercial and carries no advertising or sponsorship.</p>
"""
    return write("papers.html", shell("papers.html", "Sources", d, body,
                                      [article_ld("Sources", d, "papers.html")]))


def page_paper(key):
    p = P[key]
    d = f"{p['author_short']} ({yr(key)}), {p.get('journal','')}. {p.get('role','')}"[:300]
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
 ("Allometry", "How a trait scales with body size. Because brain mass scales predictably with body "
  "mass across mammals, a brain size change has to be assessed against body size change over the same "
  "period before any part of it can be attributed to selection on the brain itself."),
 ("Anatomically modern Homo", "Populations with skeletal features within the modern human range, "
  "appearing from roughly 300,000 years ago."),
 ("Bergmann's rule", "The observation that body mass in endothermic species tends to be larger in "
  "colder climates, a thermoregulatory principle underlying climate explanations of size change. "
  "Holds broadly in humans, with real exceptions. See the biological rules page."),
 ("Change-point analysis", "A statistical method locating where a trend shifts. The 2021 paper used it "
  "to place a brain size reduction at ~3,000 BP; the 2022 critique argued the estimate was distorted "
  "by an over-represented modern sample."),
 ("Cognitive offloading", "Storing or processing information outside the brain, in symbols, tools, "
  "writing, other people, or digital systems."),
 ("Allen's rule", "The observation that limbs and extremities are shorter in colder climates, "
  "reducing surface area relative to volume. Concerns proportion rather than mass, and survives "
  "scrutiny in humans somewhat better than Bergmann's rule does."),
 ("Cope's rule", "The tendency of evolutionary lineages to increase in body size over time. It does "
  "not describe the recent human record well. See the biological rules page."),
 ("Cranial capacity", "The internal volume of the braincase, in cubic centimetres. What fossils "
  "preserve, and hence the basis of most of this literature. Converted to brain mass via "
  "mass = 1.147 × capacity^0.976."),
 ("Encephalization quotient (EQ)", "Brain mass relative to that expected for an animal of a given body "
  "mass. Attempts to separate brain size change from body size change."),
 ("Endomorphic / ectomorphic", "Body-shape descriptors, stockier and more linear respectively. Used "
  "here for the shift toward more linear builds in warmer periods."),
 ("Holocene", "The current geological epoch, beginning about 11,700 years ago. The period in which the "
  "disputed brain size reduction is argued to have occurred."),
 ("Isometric", "Changing in direct proportion. If brain and body change isometrically, brain size "
  "change requires no separate explanation."),
 ("Interglacial", "A warm period between glacial phases. The 2025 paper finds glacial–interglacial "
  "differences in brain size only within the last 100,000 years."),
 ("Lean body mass", "Body mass excluding fat. Central to the isometry finding, since using total body "
  "mass in modern populations imports the effects of obesity into evolutionary comparisons."),
 ("Phenotypic plasticity", "Variation in how a body develops in response to conditions, within a fixed "
  "genetic range. It acts within a single lifetime, which is what separates it from evolutionary "
  "change and why the two should not be plotted on the same trend line."),
 ("Pleistocene", "The epoch from about 2.58 million to 11,700 years ago. Late Pleistocene humans had "
  "the largest brains recorded for the species."),
 ("Secular trend", "A directional change in a measured trait across recent generations, such as the "
  "rise in average height and in brain weight over the twentieth century. Secular trends are driven by "
  "nutrition, disease burden and living conditions rather than selection, and they matter here because "
  "modern measurements are the endpoint against which prehistoric samples are compared."),
 ("Stabilizing selection", "Selection favouring intermediate values and penalising extremes, proposed "
  "as what replaced directional selection for brain expansion around 300,000 years ago."),
 ("Taphonomic bias", "Distortion introduced by which remains survive to be found. Conceded by the 2023 "
  "paper as a limitation on Holocene sampling."),
]

def page_glossary():
    d = "Definitions of the technical terms used in the human brain size literature."
    items = "".join(f'<div class="qa"><h3>{html.escape(t)}</h3><p>{html.escape(x)}</p></div>' for t, x in GLOSS)
    body = f"""
<h1>Glossary</h1>
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
information, Karger's page displays three different publication dates for one article, the conflict
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

<h2>Non-commercial by requirement and by choice</h2>
<p>Two of the studies summarised here are published under Creative Commons Attribution-NonCommercial
licences, which prohibit commercial reuse. This site therefore carries no advertising, no affiliate
links, no sponsorship and no tracking. Reuse of the underlying papers follows each paper's own
licence.</p>

<h2>Corrections</h2>
<p>Errors of fact will be corrected and logged here with the date and nature of the change. Attempts
were made to be accurate and true to the original research, but wherever this site conflicts with a
research study referenced herein, it should be assumed that the journal article is more accurate.</p>
<p class="meta">No corrections have been logged. Last full review: 15 August 2026.</p>
"""
    return write("about.html", shell("about.html", "About", d, body,
                                     [article_ld("About this resource", d, "about.html")]))


# =========================================================== BUILD
def build():
    os.makedirs(OUT, exist_ok=True)
    made = [page_index(), page_debate(), page_timeline(), page_climate(), page_body(),
            page_cognition(), page_offload(), page_selfdom(), page_rules(), page_questions(), page_papers(),
            page_glossary(), page_about()]
    for k in CORE_FIVE + CONTEXT_PAPERS:
        made.append(page_paper(k))

    # ---- llms.txt / llms-full.txt -------------------------------------
    def _meta(path):
        t = open(os.path.join(OUT, path), encoding="utf-8").read()
        title = re.search(r"<h1>(.*?)</h1>", t, re.S).group(1)
        title = html.unescape(re.sub(r"<[^>]+>", "", title)).strip()
        desc = re.search(r'<meta name="description" content="(.*?)">', t, re.S).group(1)
        return title, html.unescape(desc)

    def _plaintext(path):
        t = open(os.path.join(OUT, path), encoding="utf-8").read()
        t = re.sub(r"<head>.*?</head>", "", t, flags=re.S)
        t = re.sub(r"<(script|style|nav|header|footer)[^>]*>.*?</\1>", " ", t, flags=re.S)
        t = re.sub(r"<h([1-3])[^>]*>", lambda m: "\n\n" + "#" * int(m.group(1)) + " ", t)
        t = re.sub(r"</(p|li|tr|div|h[1-6])>", "\n", t)
        t = re.sub(r"<[^>]+>", "", t)
        t = html.unescape(t)
        t = re.sub(r"[ \t]+", " ", t)
        return re.sub(r"\n{3,}", "\n\n", t).strip()

    topic = [p for p in made if "/" not in p and p != "index.html"]
    paper = [p for p in made if p.startswith("papers/")]

    lines = [f"# {SITE_NAME}", "", f"> {TAGLINE}", "",
             "A non-commercial reference on the scientific dispute over whether human brain size",
             "declined during the Holocene. Every quantitative claim is attributed to a named,",
             "DOI-linked peer-reviewed study, and where studies disagree both are cited at the point",
             "of disagreement. Positions are reported, not adjudicated.",
             "",
             "Content is free to quote with attribution to this URL. Two of the underlying papers",
             "carry CC BY-NC licences, so this resource is non-commercial and carries no advertising.",
             "", "## Overview", "",
             f"- [{_meta('index.html')[0]}]({BASE}/index.html): {_meta('index.html')[1]}",
             "", "## Topics", ""]
    for p in topic:
        t, d_ = _meta(p)
        lines.append(f"- [{t}]({BASE}/{p}): {d_}")
    lines += ["", "## Individual studies", ""]
    for p in paper:
        t, d_ = _meta(p)
        lines.append(f"- [{t}]({BASE}/{p}): {d_}")
    lines += ["", "## Optional", "",
              f"- [Full text of every page]({BASE}/llms-full.txt): the entire site as plain text.",
              f"- [Sitemap]({BASE}/sitemap.xml)", ""]
    write("llms.txt", "\n".join(lines))

    full = [f"# {SITE_NAME}", f"> {TAGLINE}",
            f"Full plain-text corpus. Source: {BASE}/  Reviewed 15 August 2026.", ""]
    for p in ["index.html"] + topic + paper:
        full += [f"\n\n{'=' * 70}\nURL: {BASE}/{p}\n{'=' * 70}\n", _plaintext(p)]
    write("llms-full.txt", "\n".join(full))

    # Preserve the former Cope's rule URL: canonical redirect, not a 404.
    for _old in ("copes-rule.html", "size-rules.html"):
        write(_old,
          '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
          '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
          "<title>Cope's rule in humans &mdash; moved</title>\n"
          '<meta name="description" content="This page has moved. Cope&#39;s rule in humans is '
          'now covered alongside Bergmann&#39;s and Allen&#39;s rules.">\n'
          f'<link rel="canonical" href="{BASE}/biological-rules.html">\n'
          '<meta http-equiv="refresh" content="0; url=biological-rules.html">\n'
          '<meta name="robots" content="noindex,follow">\n'
          "</head>\n<body>\n<h1>This page has moved</h1>\n"
          '<p>Cope&rsquo;s rule in humans is now covered at '
          '<a href="biological-rules.html">Bergmann&rsquo;s, Allen&rsquo;s and Cope&rsquo;s rules in '
          "humans</a>.</p>\n</body>\n</html>\n")

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
