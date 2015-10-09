<%def name="plugin(name, heading, extra_classes)">
    <section class="dashboard-section ${extra_classes}" id="dashboard-${name}">
    <h2>${heading}</h2>
    <div class="dash-section-content">
        ${caller.body()}
    </div>
    </section>
</%def>
