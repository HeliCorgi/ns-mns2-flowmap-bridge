import Formal.PDEBridgeAdapter

/-
CI-visible axiom audit for the strongest currently formalized bridge theorems.

These commands do not add assumptions. They print the axiom dependencies of the declarations
into the Lean build log so that unexpected dependencies are visible during review.
-/
#print axioms MNS2.affine_flowmap_bridge_of_contDiffOn_open
#print axioms MNS2.radial_flowmap_bridge_of_contDiffOn_open
#print axioms MNS2.FixedTimePDEBridgeAdapter.affine_bridge
#print axioms MNS2.FixedTimePDEBridgeAdapter.radial_bridge
#print axioms MNS2.FixedTimePDEBridgeAdapter.radial_bridge_of_zero_fixed
